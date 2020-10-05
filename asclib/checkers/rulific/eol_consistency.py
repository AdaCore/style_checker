from asclib.checkers.rulific import AbstractRuleChecker
from asclib.checkers.stringutils import PRINTABLE_EOL_MAP


class EolConsistencyRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = "eol"
    RULE_DESCRIPTION = "check that the end of lines are consistent"

    def init_context_data(self):
        self.context_last_eol = None
        self.context_error_already_reported = False

    def check_rule(self, lineno, line, eol):
        # This is the kind of error we really don't need to report
        # more than once. So if we already detected an inconsistency,
        # just return without checking any further.
        if self.context_error_already_reported:
            return

        # If this is the first time we are being called, just record
        # the kind of newline we got, and wait for the next line to
        # start checking for consistency.
        if self.context_last_eol is None:
            self.context_last_eol = eol
            return

        if eol is not None and eol != self.context_last_eol:
            assert self.context_last_eol is not None
            self.context_error_already_reported = True
            return "inconsistent newline: %s (the previous line used %s)" % (
                PRINTABLE_EOL_MAP[eol],
                PRINTABLE_EOL_MAP[self.context_last_eol],
            )
