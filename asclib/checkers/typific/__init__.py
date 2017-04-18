from asclib.checkers import FileCheckerError
from asclib.checkers.rulific.all_checkers import ALL_RULIFIC_CHECKERS
from asclib.checkers.stringutils import get_eol
from asclib.logging import log_info


class TypificChecker(object):
    def __init__(self, filename, config):
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
        """
        raise FileCheckerError(
            'abstract TypificChecker.file_type property unexpectedly called.')

    def run_external_checker(self):
        """Run an external program to check the contents of the file.

        Return a string with the corresponding error message if
        the checker discovered some issues, None otherwise.

        This is typically a tool which will perform some kind of
        language-specific check, making sure the file compiles,
        follows the proper coding style, etc.
        """
        raise FileCheckerError(
            'abstract TypificChecker.run_external_checker method'
            ' unexpectedly called.')


class TypificCheckerInfo(object):
    """Some info about the type of file a given TypificChecker handles.

    ATTRIBUTES
        comment_line_re: A regexp (string) which matches a line
            made of comment markers only (Eg: for Ada, it would
            be a line of dashes; for scripts, it would be a line
            of '#' characters). None if checkers should not worry
            about that aspect.
        ada_RM_spec_p: True if the file to be checked is an Ada RM
            spec, False otherwise.
        copyright_box_r_edge_re: If this type of file has copyright
            notices enclosed inside an ascii-art box, this attribute
            should be a regexp (string) matching the right edge of
            that box. None otherwise.
    """
    def __init__(self, comment_line_re, ada_RM_spec_p,
                 copyright_box_r_edge_re):
        self.comment_line_re = comment_line_re
        self.ada_RM_spec_p = ada_RM_spec_p
        self.copyright_box_r_edge_re = copyright_box_r_edge_re
