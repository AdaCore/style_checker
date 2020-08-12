import pytest


def test_bad_file_checker(style_checker):
    """Check behavior when pep8 is missing
    """
    style_checker.enable_unit_test()

    # Derive the TypificChecker class without providing the mandatory
    # methods which are otherwise abstract.
    from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
    from asclib.checkers.rulific.all_checkers import ALL_RULIFIC_CHECKERS

    class BadFileChecker(TypificChecker):
        # Do provide a complete rulific_decision_map attribute, though,
        # as the contents of that dictionary is checked during
        # the object's initialization.
        rulific_decision_map = dict(
            (checker.RULE_CONFIG_NAME, False)
            for checker in ALL_RULIFIC_CHECKERS)
        # Same the typific_info attribute...
        typific_info = TypificCheckerInfo(comment_line_re='#',
                                          ada_RM_spec_p=False,
                                          copyright_box_r_edge_re=None)

    bad_checker = BadFileChecker('src/simple.py', None)

    # Now verify that calling those methods cause an exception.
    from asclib.checkers import FileCheckerError
    with pytest.raises(FileCheckerError) as cm:
        print(bad_checker.file_type)
    expected_output = \
        'abstract TypificChecker.file_type property unexpectedly called.'
    style_checker.assertOutputEqual(expected_output, str(cm.value))

    with pytest.raises(FileCheckerError) as cm:
        bad_checker.run_external_checker()
    expected_output = \
        'abstract TypificChecker.run_external_checker method' \
        ' unexpectedly called.'
    style_checker.assertOutputEqual(expected_output, str(cm.value))


def test_missing_entry_in_rulific_decision_map(style_checker):
    """Test when missing an entry in rulific_decision_map.
    """
    style_checker.enable_unit_test()

    # Derive the TypificChecker class only providing some of
    # the mandatory overrides. In particular, only provide
    # an incomplete rulific_decision_map attribute, so as to
    # make sure we get an error when trying to instantiate
    # that broken class.
    #
    # We also need to provide the file_type attribute as it is used
    # to produce a human-readable error message.
    from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
    from asclib.checkers.rulific.all_checkers import ALL_RULIFIC_CHECKERS

    class IncompleteFileChecker(TypificChecker):
        rulific_decision_map = dict(
            (checker.RULE_CONFIG_NAME, False)
            for checker in ALL_RULIFIC_CHECKERS[:-1])
        typific_info = TypificCheckerInfo(comment_line_re='#',
                                          ada_RM_spec_p=False,
                                          copyright_box_r_edge_re=None)
        file_type = 'Python script'

    # Now verify that calling those methods cause a failed
    # assertion.
    with pytest.raises(AssertionError) as cm:
        IncompleteFileChecker('src/simple.py', None)
    expected_output = \
        'Python script checker missing config about' \
        ' %s rule' % ALL_RULIFIC_CHECKERS[-1].RULE_CONFIG_NAME
    style_checker.assertOutputEqual(expected_output, str(cm.value))
