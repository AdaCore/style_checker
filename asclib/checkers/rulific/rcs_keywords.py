from asclib.checkers.rulific import AbstractRuleChecker


class RCSKeywordsRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = "no_rcs_keywords"
    RULE_DESCRIPTION = "check that we do not have old RCS keywords"

    def check_rule(self, lineno, line, eol):
        # Use string concatenation to create the pattern we are
        # looking for, so as to avoid tripping this style check
        # on this file!
        if "$" + "Revision: " in line:
            return "RCS Revision keyword not allowed"
