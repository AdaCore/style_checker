from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
from asclib.ex import Run


class ShFileChecker(TypificChecker):
    rulific_decision_map = {
        'copyright': False,
        'eol': True,
        'first_line_comment': False,
        'max_line_length': False,
        'no_dos_eol': True,
        'no_last_eol': True,
        'no_rcs_keywords': False,
        'no_tab_indent': False,
        'no_trailing_space': True,
        }

    typific_info = TypificCheckerInfo(comment_line_re=None,
                                      ada_RM_spec_p=False,
                                      copyright_box_r_edge_re=None)

    @property
    def file_type(self):
        return 'sh script'

    def run_external_checker(self):
        try:
            p = Run(['/bin/sh', '-n', self.filename])
            if p.status != 0:
                return p.out
        except OSError as e:  # pragma: no cover (see below)
            # Can only really happen if sh is not installed on the host
            # machine. Near-zero probability, but we keep this handler
            # so as to generate an error message rather than a traceback.
            return 'Failed to run sh: %s' % e
