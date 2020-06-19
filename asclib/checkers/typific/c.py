from asclib.checkers.typific import TypificChecker, TypificCheckerInfo


class CFileChecker(TypificChecker):
    rulific_decision_map = {
        'copyright': True,
        'eol': True,
        'first_line_comment': False,
        'max_line_length': False,
        'no_dos_eol': True,
        'no_last_eol': True,
        'no_rcs_keywords': True,
        'no_tab_indent': False,
        'no_trailing_space': True,
    }

    typific_info = TypificCheckerInfo(
        comment_line_re=None,
        ada_RM_spec_p=False,
        copyright_box_r_edge_re=None)

    @property
    def file_type(self):
        return 'C'

    def run_external_checker(self):
        # Nothing to do.
        pass
