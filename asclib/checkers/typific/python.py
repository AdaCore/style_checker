from gnatpython.ex import Run
import re

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo


class PythonFileChecker(TypificChecker):
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

    typific_info = TypificCheckerInfo(comment_line_re='##*',
                                      ada_RM_spec_p=False,
                                      copyright_box_r_edge_re=None)

    @property
    def file_type(self):
        return 'Python script'

    def run_external_checker(self):
        # PEP8 checks are disabled for this file is we find a specific
        # string in the first 2 lines of the file...
        with open(self.filename) as f:
            for lineno in (1, 2):
                line = f.readline()
                if line and re.match('^# No_Style_Check$', line) is not None:
                    # ??? VERBOSE...
                    return

        try:
            p = Run(['pep8', '-r',
                     '--ignore=E121,E123,E126,E226,E24,E704,E402',
                     self.filename])
            if p.status != 0 or p.out:
                return p.out
        except OSError as e:
            return 'Failed to run pep8: %s' % e
