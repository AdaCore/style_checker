from asclib.checkers import FileCheckerError
from asclib.checkers.rulific.all_checkers import ALL_RULIFIC_CHECKERS
from asclib.checkers.stringutils import get_eol
from asclib.logging import log_info


class TypificChecker(object):
    """The style checker for a given file type.

    :ivar filename: The name of the file to check.
    :ivar config: A Config object.
    :iver my_rulific_checkers: The list of rulific checkers this
        typific checker will be using, in the same order as in
        ALL_RULIFIC_CHECKERS.
    """
    def __init__(self, filename, config):
        """The constructor.

        :param filename: Same as the attribute.
        :type filename: str
        :param config: Same as the attribute.
        :type config: Config
        """
        self.filename = filename
        self.config = config

        # Sanity check the contents of self.rulific_decision_map,
        # which is expected to be set/overriden by the child class.
        # The purpose of this change is to make sure child class
        # insn't missing an entry for one of the checkers.
        for rulific_checker in ALL_RULIFIC_CHECKERS:
            assert (rulific_checker.RULE_CONFIG_NAME in
                    self.rulific_decision_map), \
                '%s checker missing config about %s rule' % (
                    self.file_type, rulific_checker.RULE_CONFIG_NAME)

        # Build the list of checkers we actually want to run
        # for this file using rulific_decision_map
        # to decide.
        self.my_rulific_checkers = [
            rulific_checker(self.filename, self.config, self.typific_info)
            for rulific_checker in ALL_RULIFIC_CHECKERS
            if (self.rulific_decision_map[rulific_checker.RULE_CONFIG_NAME] and
                '-' + rulific_checker.RULE_CONFIG_NAME not
                in self.config.options)]

        # Initialize the various rulific checkers we selected.
        for rulific_checker in self.my_rulific_checkers:
            rulific_checker.init_context_data()

        # Verify the child class did not forget to override
        # the typific_info class attribute.
        assert self.typific_info is not None, \
            '%s checker not defined properly (no typific_info)' % \
            self.file_type

    def check_file(self):
        """Perform all necessary checks on our file (including rulific ones).

        Raise FileCheckerError if an error is detected.

        :return: None.
        :rtype: None
        """
        log_info("Checking style of `%s' (%s)"
                 % (self.filename, self.file_type))

        # Build the error message into a list. And then, at the end of
        # this function, if it turns out we got at least one issue,
        # raise it via FileCheckerError.
        err_msgs = []

        # First, run the external checker...
        external_checker_err_msg = self.run_external_checker()
        if external_checker_err_msg is not None:
            # Stop immediately if the external checker detected some
            # errors.  We could continue, and run the rest of the
            # tests, but cvs_check, the previous style checker,
            # wasn't doing that, so we don't either so as to be
            # consistent with the traditional behavior.
            raise FileCheckerError(external_checker_err_msg)

        # First, feed line-by-line the contents of the file to each
        # rulific checker.
        with open(self.filename) as f:
            for lineno, line in enumerate(f, 1):
                eol = get_eol(line)
                line = line[:-len(eol or '')]
                for rulific_checker in self.my_rulific_checkers:
                    rulific_checker.process_line(lineno, line, eol)

        # Merge all the result of the line-by-line checking, currently
        # stored in each rulific checker, into a combined dictionary,
        # where# keys are still line numbers, but the value is a list
        # of error messages applying to that line number.
        all_linenos = sorted(
            set().union(*(rulific_checker.errors_found.keys()
                          for rulific_checker in self.my_rulific_checkers)))
        for lineno in all_linenos:
            for rulific_checker in self.my_rulific_checkers:
                if lineno in rulific_checker.errors_found:
                    err_msgs.append('%s:%d: %s'
                                    % (self.filename, lineno,
                                       rulific_checker.errors_found[lineno]))

        for rulific_checker in self.my_rulific_checkers:
            global_check_err_msg = rulific_checker.global_check()
            if global_check_err_msg:
                err_msgs.append(global_check_err_msg)

        if err_msgs:
            raise FileCheckerError(*err_msgs)

    def dump_checks(self, cvs_check_file_type, print_header=False,
                    print_footer=False):
        """Dump to stdout the rulific_decision_map for our type of file.

        The purpose is to be able to compare the rulific_decision_map
        against the same map from cvs_check, so as to make sure they
        are the same.  So we need to print them in the same order as
        cvs_check.

        :param cvs_check_file_type: The file type as described by
            cvs_check (the legacy style checker this tool is replacing)
            equivalent to this object's file type.
        :type cvs_check_file_type: str
        :param print_header: If True, then print a table header displaying
            the name of each rulific checker.
        :type print_header: bool
        """
        from asclib.checkers.rulific.copyright import CopyrightRuleChecker
        from asclib.checkers.rulific.rcs_keywords import RCSKeywordsRuleChecker
        from asclib.checkers.rulific.dos_eol import DosEolRuleChecker
        from asclib.checkers.rulific.eol_consistency \
            import EolConsistencyRuleChecker
        from asclib.checkers.rulific.first_line_comment \
            import FirstLineCommentRuleChecker
        from asclib.checkers.rulific.last_line_eol \
            import LastLineEOLRuleChecker
        from asclib.checkers.rulific.line_length import LineLengthRuleChecker
        from asclib.checkers.rulific.trailing_spaces \
            import TrailingSpaceRuleChecker

        RULES_LIST = (
            ('STYLE', None),
            ('FEATURES', None),
            ('START_COMMENT', FirstLineCommentRuleChecker),
            ('START_BANG', None),
            ('COPYRIGHT', CopyrightRuleChecker),
            ('ADA_RM_SPEC', None),
            ('EOL', EolConsistencyRuleChecker),
            ('NO_DOS_EOL', DosEolRuleChecker),
            ('NO_LAST_EOL', LastLineEOLRuleChecker),
            ('LENGTH', LineLengthRuleChecker),
            ('TRAILING', TrailingSpaceRuleChecker),
            ('REV', RCSKeywordsRuleChecker))

        if print_header:
            print(' ' * 11 +
                  ' '.join(['{:^6}'.format(cvs_check_name[:6])
                            for (cvs_check_name, _) in RULES_LIST]).rstrip())

        checks_status = []
        for cvs_check_name, rulific_checker in RULES_LIST:
            if cvs_check_name == 'ADA_RM_SPEC':
                # Special case, where we have to to dig into
                # the typific_info rather than the rulific_decision_map.
                checks_status.append('X' if self.typific_info.ada_RM_spec_p
                                     else '-')
            elif rulific_checker is None:
                checks_status.append(' ')
            else:
                rulific_name = rulific_checker.RULE_CONFIG_NAME
                checks_status.append(
                    'X' if self.rulific_decision_map[rulific_name]
                    else '-')
        print('{:10.10}   {}'.format(cvs_check_file_type,
                                     '      '.join(checks_status)))

        if print_footer:
            print('\nLegend:')
            print('-------')
            for cvs_check_name, rulific_checker in RULES_LIST:
                if rulific_checker is None:
                    continue
                print('  %s: %s' % (cvs_check_name,
                                    rulific_checker.RULE_DESCRIPTION))

    ######################################################################
    #  Abstract methods/attributes/properties:
    #
    #  Child classes are expected to override the following methods
    #  For the proper functionning of the actual class.
    ######################################################################

    # A dictionary, which is expected to contain a key corresponding
    # to the RULE_CONFIG_NAME of each checker in ALL_RULIFIC_CHECKERS.
    # The value for that key is either True if the checker should be
    # executed for that type of file, or False if not.
    #
    # We do not provide a default value to make sure that all child
    # classes explicitly decide whether or not to use each rulific
    # checker.
    rulific_decision_map = {}

    # A TypificCheckerInfo object, instantiated for the particular
    # kind of typific checker.
    typific_info = None

    @property
    def file_type(self):
        """Return a string describing the kind of file this checker applies to.

        NOTE: This was turned into a property so as to allow checkers
        to handle multiple kinds of files.  This can be useful when
        there are only very slight variations on how the set of files
        is checked (Eg: with Ada, the compiler units typically have
        some extra checks).  As such, a class attribute would not have
        worked in this context.

        :rtype: str
        """
        raise FileCheckerError(
            'abstract TypificChecker.file_type property unexpectedly called.')

    def run_external_checker(self):
        """Run an external program to check the contents of the file.

        This is typically a tool which will perform some kind of
        language-specific check, making sure the file compiles,
        follows the proper coding style, etc.

        :return: A string with the corresponding error message if
            the checker discovered some issues, None otherwise.
        :rtype: str | None
        """
        raise FileCheckerError(
            'abstract TypificChecker.run_external_checker method'
            ' unexpectedly called.')


class TypificCheckerInfo(object):
    """Some info about the type of file a given TypificChecker handles.

    :ivar comment_line_re: A regexp (string) which matches a line
        made of comment markers only (Eg: for Ada, it would be a line
        of dashes; for scripts, it would be a line of '#' characters).
        None if checkers should not worry about that aspect.
    :ivar ada_RM_spec_p: True if the file to be checked is an Ada RM
        spec, False otherwise.
    :ivar copyright_box_r_edge_re: If this type of file has copyright
        notices enclosed inside an ascii-art box, this attribute should
        be a regexp (string) matching the right edge of that box.
        None otherwise.
    """
    def __init__(self, comment_line_re, ada_RM_spec_p,
                 copyright_box_r_edge_re):
        """The constructor.

        :param comment_line_re: Same as the attribute.
        :type comment_line_re: str | None
        :param ada_RM_spec_p: Same as the attribute.
        :type ada_RM_spec_p: bool
        :param copyright_box_r_edge_re: Same as the attribute.
        :type copyright_box_r_edge_re: str | None
        """
        self.comment_line_re = comment_line_re
        self.ada_RM_spec_p = ada_RM_spec_p
        self.copyright_box_r_edge_re = copyright_box_r_edge_re
