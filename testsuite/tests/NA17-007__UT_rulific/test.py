from support import *

class TestRun(TestCase):
    def test_missing_check_rule_override(self):
        """calling AbstractRuleChecker.check_rule.

        Test that AbstractRuleChecker.check_rule behaves as expected.
        """
        self.enable_unit_test()

        from asclib.checkers.rulific import AbstractRuleChecker
        from asclib.checkers import FileCheckerError

        class BadRuleChecker(AbstractRuleChecker):
            RULE_CONFIG_NAME = 'bad rule'
            RULE_DESCRIPTION = 'a bad rule'

        with self.assertRaises(FileCheckerError) as cm:
            rule_checker = BadRuleChecker('filename', None, None)
            rule_checker.check_rule(1, 'hello', '\n')
        expected_output = 'abstract RuleChecker.check_rule method called'
        self.assertOutputEqual(expected_output, str(cm.exception))


if __name__ == '__main__':
    runtests()
