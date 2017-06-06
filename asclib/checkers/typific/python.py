from gnatpython.ex import Run
import re

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo

PYTHON_FILE_TYPE = 'Python script'
PLAN_FILE_TYPE = 'Electrolyt plan'


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
        if self.filename.endswith('.plan'):
            return PLAN_FILE_TYPE
        else:
            return PYTHON_FILE_TYPE

    def run_external_checker(self):
        # Style checks are disabled for this file is we find a specific
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

        if self.__run_pyflakes():
            try:
                p = Run(['pyflakes', self.filename])
                if p.status != 0 or p.out:
                    return p.out
            except OSError as e:
                return 'Failed to run pyflakes: %s' % e

    def __run_pyflakes(self):
        """Return True iff we should run pyflakes to validate our file.
        """
        # Run pyflakes on every files except .plan files, for which we
        # know legitimate scripts would still fail this checker.
        return self.file_type != PLAN_FILE_TYPE
