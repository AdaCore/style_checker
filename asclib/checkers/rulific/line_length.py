from asclib.checkers.rulific import AbstractRuleChecker

# The maximum line length.
MAX_COL = 79


class LineLengthRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = 'max_line_length'
    RULE_DESCRIPTION = \
        'check that lines are not too long (%d characters)' % MAX_COL

    def check_rule(self, lineno, line, eol):
        line_len = len(line)
        if line_len > MAX_COL:
            return ('this line is too long (%d > %d characters)'
                    % (line_len, MAX_COL))
