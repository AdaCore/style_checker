from asclib.checkers.rulific import AbstractRuleChecker
import re


class NoTabIndentationRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = 'no_tab_indent'
    RULE_DESCRIPTION = 'check that tab characters are not used for indentation'
    SPACES_TAB_MATCHER = re.compile(r'\s*\t')

    def check_rule(self, lineno, line, eol):
        m = self.SPACES_TAB_MATCHER.match(line)
        if m is not None:
            return 'Indentation must not use Tab characters'
