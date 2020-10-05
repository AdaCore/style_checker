from asclib.checkers.rulific import AbstractRuleChecker
from asclib.checkers.stringutils import DOS_EOL


class DosEolRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = "no_dos_eol"
    RULE_DESCRIPTION = "check that we do not have DOS end-of-line sequences"

    def check_rule(self, lineno, line, eol):
        if eol == DOS_EOL:
            return "DOS line ending is not allowed"
