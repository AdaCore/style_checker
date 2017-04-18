from support import *

class TestRun(TestCase):
    def test_bad_file_checker(self):
        """Check behavior when pep8 is missing
        """
        self.enable_unit_test()

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
        with self.assertRaises(FileCheckerError) as cm:
            print bad_checker.file_type
        expected_output = \
            'abstract TypificChecker.file_type property unexpectedly called.'
        self.assertOutputEqual(expected_output, str(cm.exception))

        with self.assertRaises(FileCheckerError) as cm:
            bad_checker.run_external_checker()
        expected_output = \
            'abstract TypificChecker.run_external_checker method' \
            ' unexpectedly called.'
        self.assertOutputEqual(expected_output, str(cm.exception))

    def test_missing_entry_in_rulific_decision_map(self):
        """Test when missing an entry in rulific_decision_map.
        """
        self.enable_unit_test()

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
        with self.assertRaises(AssertionError) as cm:
            bad_checker = IncompleteFileChecker('src/simple.py', None)
        expected_output = \
            'Python script checker missing config about' \
            ' %s rule' % ALL_RULIFIC_CHECKERS[-1].RULE_CONFIG_NAME
        self.assertOutputEqual(expected_output, str(cm.exception))


if __name__ == '__main__':
    runtests()
