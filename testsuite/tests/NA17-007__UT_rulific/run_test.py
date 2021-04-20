import pytest


def test_missing_check_rule_override(style_checker):
    """calling AbstractRuleChecker.check_rule.

    Test that AbstractRuleChecker.check_rule behaves as expected.
    """
    style_checker.enable_unit_test()

    from asclib.checkers.rulific import AbstractRuleChecker
    from asclib.checkers import FileCheckerError

    class BadRuleChecker(AbstractRuleChecker):
        RULE_CONFIG_NAME = 'bad rule'
        RULE_DESCRIPTION = 'a bad rule'

    with pytest.raises(FileCheckerError) as cm:
        rule_checker = BadRuleChecker('filename', None, None)
        rule_checker.check_rule(1, 'hello', '\n')
    expected_output = 'abstract RuleChecker.check_rule method called'
    style_checker.assertOutputEqual(expected_output, str(cm.value))
