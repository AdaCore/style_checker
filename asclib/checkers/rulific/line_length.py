from asclib.checkers.rulific import AbstractRuleChecker

# The maximum line length.
MAX_COL = 79


class LineLengthRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = 'max_line_length'
    RULE_DESCRIPTION = \
        'check that lines are not too long (%d characters)' % MAX_COL

    def check_rule(self, lineno, line, eol):
        l = len(line)
        if l > MAX_COL:
            return ('this line is too long (%d > %d characters)'
                    % (l, MAX_COL))
