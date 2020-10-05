import os
import re
import sys

from asclib import get_prefix_dir
from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
from asclib.ex import Run

PYTHON_FILE_TYPE = "Python script"
PYTHON_FRAGMENT_FILE_TYPE = "Python fragment"
PLAN_FILE_TYPE = "Electrolyt plan"

# The list errors that we want flake8 to ignore (in addition to
# the errors that flake8 already ignores by default).
EXTEND_IGNORE_LIST = (
    # Pycodestyle: E402: module level import not at top of file
    #
    # Rationale: See Q721-011: We sometimes need to import sys,
    # and then update sys.path before we can start importing
    # some other modules.
    "E402",
)

# The maximum line length. We change the default length to match
# the default from "black" (a code reformatter) [T819-027].
MAX_LINE_LENGTH = 88


class PythonFileChecker(TypificChecker):
    rulific_decision_map = {
        "copyright": False,
        "eol": True,
        "first_line_comment": False,
        "max_line_length": False,
        "no_dos_eol": True,
        "no_last_eol": True,
        "no_rcs_keywords": False,
        "no_tab_indent": False,
        "no_trailing_space": True,
    }

    typific_info = TypificCheckerInfo(
        comment_line_re="##*", ada_RM_spec_p=False, copyright_box_r_edge_re=None
    )

    @property
    def file_type(self):
        if self.filename.endswith(".plan"):
            return PLAN_FILE_TYPE
        elif self.filename.endswith(".frag.py"):
            return PYTHON_FRAGMENT_FILE_TYPE
        else:
            return PYTHON_FILE_TYPE

    def run_external_checker(self):
        # Check the first two lines of the file, and scan for certain
        # specific keywords indicating possible special treatment for
        # this file.
        python_fragment_p = False
        with open(self.filename) as f:
            for _unused_lineno in (1, 2):
                line = f.readline()
                if line and re.match("^# No_Style_Check$", line) is not None:
                    # ??? VERBOSE...
                    return
                elif (
                    line
                    and re.match("^# Style_Check:Python_Fragment", line, re.I)
                    is not None
                ):
                    python_fragment_p = True

        p = Run(
            [
                sys.executable,
                "-m",
                "pycodestyle",
                "--config=" + os.path.join(get_prefix_dir(), "etc", "pycodestyle.cfg"),
                self.filename,
            ]
        )
        if p.status != 0 or p.out:
            return p.out

        if not python_fragment_p and self.__run_pyflakes():
            p = Run([sys.executable, "-m", "pyflakes", self.filename])
            if p.status != 0 or p.out:
                return p.out

    def __run_pyflakes(self):
        """Return True iff we should run pyflakes to validate our file."""
        # We want to run pyflakes on every file, except that there are
        # kinds of file that legitimately fail this checker. Exclude
        # those.
        return self.file_type not in (PYTHON_FRAGMENT_FILE_TYPE, PLAN_FILE_TYPE)
