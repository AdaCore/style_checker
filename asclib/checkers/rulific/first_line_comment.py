from asclib.checkers.rulific import AbstractRuleChecker
import re


class FirstLineCommentRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = 'first_line_comment'
    RULE_DESCRIPTION = 'check that the first line is a comment'

    def init_context_data(self):
        # This checker shouldn't even be enabled if the typific_info
        # doesn't contain a non-empty comment_line_re (meaning we don't
        # want to worry about comments).  Do this check in this method
        # even though technically it's not actually initializing any
        # context data. But it allows us to perform the check only
        # once for the entire lifetime of the checker.
        assert self.typific_info.comment_line_re, \
            'comment_line_re info missing in first_line_comment rule checker'

    def check_rule(self, lineno, line, eol):
        if lineno > 1:
            # We only need to check the first line...
            return
        if not re.match(self.typific_info.comment_line_re, line):
            if self.typific_info.comment_line_re.endswith('$'):
                return 'First line must be comment markers only.'
            else:
                return 'First line must start with a comment (regexp: %s)' % \
                    self.typific_info.comment_line_re
