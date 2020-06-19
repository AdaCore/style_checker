from asclib.checkers import FileCheckerError


class AbstractRuleChecker(object):
    """A checker to apply to all (text-based) files.

    :ivar filename: The name of the file to perform style checks on.
    :ivar config: A Config object.
    :ivar typific_info: A TypificCheckerInfo object.
    :ivar errors_found: A dictionary, indexed by line number, whose value
        is a string describing an error detected on that line.
    :ivar more_errors_found: True if there are more errors than the ones
        listed in the errors_found dictionary above, and we stopped adding
        the new ones because we exceeded the number of such errors we wanted
        to report.
    """

    # The name of the rule, as identified in the style-checker
    # config file.  This is what the style-check can use to determine
    # whether a given checker should be applied or not.
    #
    # Child classes must all set this.
    RULE_CONFIG_NAME = None

    # The description of that rule.  All child classes must override this.
    RULE_DESCRIPTION = None

    # The maximum number of times we report the same error, after which
    # we just tell the user there are more errors in his file he needs
    # to correct.  This is to avoid flooding the output with the same
    # error over and over again (eg: wrong line-ending in a super long
    # file).
    MAX_REPORTING_PER_CHECKER = 3

    # By default, the process_line method stops feeding the contents
    # of the file to be checked as soon as we found more errors than
    # we care to report (MAX_REPORTING_PER_CHECKER). But there are
    # situations were the checker might need to be given the entire
    # file before deciding whether the rule has been followed or not
    # These checkers are expected to change the following class attribute
    # to False.
    STOP_READING_FILE_AFTER_TOO_MANY_ERRORS = True

    def __init__(self, filename, config, typific_info):
        """The constructor.

        :param filename: Same as the attribute.
        :type filename: str
        :param config: Same as the attribute.
        :type config: Config
        :param typific_info: Same as the attribute.
        :type typific_info: TypificCheckerInfo
        """
        assert self.RULE_CONFIG_NAME is not None
        assert self.RULE_DESCRIPTION is not None
        self.filename = filename
        self.config = config
        self.typific_info = typific_info
        self.errors_found = {}
        self.more_errors_found = False

    def init_context_data(self):
        """Initialize all necessary data needed to perform the rule check.

        Child classes that need to save some context data should override
        this method, and create the data structures they need in order
        to perform their checks, and save this data in self as attributes.
        To avoid attribute collisions, attribute names starting with
        with context are reserved for this specific usage.
        FIXME: Why not use namespaces???

        By default, this method does nothing.
        """
        pass

    def process_line(self, lineno, line, eol):
        """Process the given line from the file being checked.

        The file to be checked is read line by line, and this function
        gets called once for each line, in order.

        :param lineno: The line number of the line being processed.
        :type lineno: int
        :param line: The line being processed, minus the end-of-line
            marker (if any).
        :type line: str
        :param eol: The end-of-line marker if the given line had one
            in the file being checked, or None if there wasn't any.
        :type eol: str | None
        """
        if self.STOP_READING_FILE_AFTER_TOO_MANY_ERRORS and \
                self.more_errors_found:
            # No need to look for more errors; we would not be reporting
            # those additional errors anyway.
            return

        err_msg = self.check_rule(lineno, line, eol)
        if err_msg:
            if len(self.errors_found.keys()) < self.MAX_REPORTING_PER_CHECKER:
                self.errors_found[lineno] = err_msg
            elif not self.more_errors_found:
                # It is the first error over the threshold, so record
                # the fact that we actually exceeded the threshold, and
                # amend the error message from the last time we detected
                # the rule violation to mention the fact that more errors
                # were detected, but are no longer reported (for brevity).
                self.more_errors_found = True
                last_err_lineno = sorted(self.errors_found.keys())[-1]
                self.errors_found[last_err_lineno] += \
                    ' [similar errors no longer shown]'

    def check_rule(self, lineno, line, eol):
        """Report an error the given line contains a style violation.

        This is an abstract method which we expect child classes
        to override.

        :param lineno: Same as self.process_line.
        :type lineno: int
        :param line: Same as self.process_line.
        :type line: str
        :param eol: Same as self.process_line.
        :type eol: str | None

        :return: A string with the error message if a violation is detected.
            None otherwise.
        :rtype: str | None
        """
        raise FileCheckerError(
            'abstract RuleChecker.check_rule method called')

    def global_check(self):
        """Report errors only detectable after having read the entire file.

        By default, do nothing. Child classes which need a global view
        of the file's content in order to determine whether the file
        passes the checks or not should override this method.

        :return: Same as self.check_rule.
        :rtype: str | None
        """
        return None
