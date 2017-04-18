from gnatpython.ex import Run

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo


class CshFileChecker(TypificChecker):
    rulific_decision_map = {
        'copyright': False,
        'eol': True,
        'first_line_comment': False,
        'max_line_length': False,
        'no_dos_eol': True,
        'no_last_eol': True,
        'no_rcs_keywords': False,
        'no_trailing_space': True,
        }

    typific_info = TypificCheckerInfo(comment_line_re=None,
                                      ada_RM_spec_p=False,
                                      copyright_box_r_edge_re=None)

    @property
    def file_type(self):
        return 'csh script'

    def run_external_checker(self):
        try:
            p = Run(['/bin/csh', '-n', self.filename])
            if p.status != 0:
                return p.out
        except OSError as e:
            return 'Failed to run csh: %s' % e
