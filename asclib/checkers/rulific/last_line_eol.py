from asclib.checkers.rulific import AbstractRuleChecker


class LastLineEOLRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = "no_last_eol"
    RULE_DESCRIPTION = "check that the last line as a line-ending"

    def init_context_data(self):
        self.context_last_line_eol = None
        self.context_last_lineno = 0

    def check_rule(self, lineno, line, eol):
        self.context_last_line_eol = eol
        self.context_last_lineno = lineno

    def global_check(self):
        if self.context_last_lineno > 0 and self.context_last_line_eol is None:
            return "%s:%d: no newline at end of file" % (
                self.filename,
                self.context_last_lineno,
            )
