import re

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
from asclib.ex import Run

PYTHON_FILE_TYPE = 'Python script'
PYTHON_FRAGMENT_FILE_TYPE = 'Python fragment'
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
        elif self.filename.endswith('.frag.py'):
            return PYTHON_FRAGMENT_FILE_TYPE
        else:
            return PYTHON_FILE_TYPE

    def run_external_checker(self):
        # Check the first two lines of the file, and scan for certain
        # specific keywords indicating possible special treatment for
        # this file.
        python_fragment_p = False
        with open(self.filename) as f:
            for lineno in (1, 2):
                line = f.readline()
                if line and re.match('^# No_Style_Check$', line) is not None:
                    # ??? VERBOSE...
                    return
                elif line and re.match('^# Style_Check:Python_Fragment',
                                       line, re.I) is not None:
                    python_fragment_p = True

        try:
            p = Run(['pep8', '-r',
                     '--ignore=E121,E123,E126,E226,E24,E704,E402',
                     self.filename])
            if p.status != 0 or p.out:
                return p.out
        except OSError as e:
            return 'Failed to run pep8: %s' % e

        if not python_fragment_p and self.__run_pyflakes():
            try:
                p = Run(['pyflakes', self.filename])
                if p.status != 0 or p.out:
                    return p.out
            except OSError as e:
                return 'Failed to run pyflakes: %s' % e

    def __run_pyflakes(self):
        """Return True iff we should run pyflakes to validate our file.
        """
        # We want to run pyflakes on every file, except that there are
        # kinds of file that legitimately fail this checker. Exclude
        # those.
        return self.file_type not in (PYTHON_FRAGMENT_FILE_TYPE,
                                      PLAN_FILE_TYPE)
