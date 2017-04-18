from asclib.checkers.rulific import AbstractRuleChecker


class TrailingSpaceRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = 'no_trailing_space'
    RULE_DESCRIPTION = 'check that we have no trailing whitespaces'

    def check_rule(self, lineno, line, eol):
        if len(line) > 0 and line[-1:] in (' ', '\t'):
            # Note that we can't use isspace to double-check for
            # the trailing whitespace, because, in Python, characters
            # such as \f (aka ^L) and \v are also considered whitespaces,
            # while we don't want to flag these as trailing whitespaces.
            # So only consider trailing spaces and tabs as invalid.
            return 'Trailing spaces are not allowed'
