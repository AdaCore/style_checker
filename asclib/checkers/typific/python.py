import re
import sys

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
from asclib.ex import Run

PYTHON_FILE_TYPE = "Python script"
PYTHON_FRAGMENT_FILE_TYPE = "Python fragment"
PLAN_FILE_TYPE = "Electrolyt plan"

# The list of errors that we want flake8 to ignore (in addition to
# the errors that flake8 already ignores by default), for all
# types of Python files.
EXTEND_IGNORE_LIST_ALL = (
    # E203: whitespace before ':'
    #
    # The purpose of this rule is to warn against situations such as...
    #
    #      with open(filename) as f :
    #                              ^
    #                              +--- Unexpected whitespace here.
    #
    # ... but unfortunately, this rule triggers a false positive
    # for array slices when formatted by black. E.g:
    #
    #      buf[match.end(0) :]
    #                      ^
    #                      +--- Space here, inserted by black.
    #
    # More and more repositories are trying to adopt black, and combine
    # this with the use of pre-commit scripts that ensure files are
    # always properly formatted. To help teams active that without
    # disabling the server-side precommit checks entirely, we disable
    # this specific rule.
    #
    # Note also that it appears that this E203 warning in this case
    # appears to be considered a pycodestyle bug. But unfortunately
    # it's been a fairly longstanding one, and it's unclear to me
    # whether there is any chance of this bug being solved anytime soon.
    # For more details, see:
    # https://github.com/PyCQA/pycodestyle/issues/373
    "E203",

    # flake8: E402: module level import not at top of file
    #
    # Rationale: See Q721-011: We sometimes need to import sys,
    # and then update sys.path before we can start importing
    # some other modules.
    "E402",
)

# When checking Python files that might be incomplete (e.g "Python fragment"
# files, or Electrolyt Plan files, the additional list of errors we want
# to ignore (this is in addition to the errors listed in EXTEND_IGNORE_LIST_ALL).
EXTEND_IGNORE_LIST_INCOMPLETE_PYTHON = (
    # flake8: F821: undefined name "<name_of_entity>"
    #
    # Rationale: See Q620-021: That entity can legitimately be declared elsewhere.
    "F821",
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

        extend_ignore = list(EXTEND_IGNORE_LIST_ALL)
        if python_fragment_p or self.__incomplete_python_file_p():
            extend_ignore.extend(EXTEND_IGNORE_LIST_INCOMPLETE_PYTHON)

        p = Run(
            [
                sys.executable,
                "-m",
                "flake8",
                f"--max-line-length={MAX_LINE_LENGTH}",
                "--extend-ignore={}".format(",".join(extend_ignore)),
                self.filename,
            ]
        )
        if p.status != 0 or p.out:
            return p.out

    def __incomplete_python_file_p(self):
        """Return True if checking a Python file which may not be self-sufficient.

        This method checks our file_type attributes, to determine whether
        we expect the file to be checked to be complete and self-sufficient.
        If not, return True. Otherwise, return False.

        See EXTEND_IGNORE_LIST_INCOMPLETE_PYTHON for more information about
        the intent behind identifying such files.
        """
        return self.file_type in (PYTHON_FRAGMENT_FILE_TYPE, PLAN_FILE_TYPE)
