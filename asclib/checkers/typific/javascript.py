import re

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
from asclib.ex import Run


class JavascriptFileChecker(TypificChecker):
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

    # The list of modules for which JsDoc annotations are allowed
    # (we default is to reject them).
    MODULES_WITH_JSDOC = ('qmachine',
                          'modeling',
                          'web-components')

    @property
    def file_type(self):
        return 'Javascript'

    def run_external_checker(self):
        # For these kinds of files, the external check should be
        # disabled if there is a "No_Style_Check" comment starting
        # either the first or the second line.
        with open(self.filename) as f:
            for lineno in (1, 2):
                line = f.readline()
                if line and re.match('^// No_Style_Check$', line) is not None:
                    # ??? VERBOSE...
                    return
        jslint_cmd = ['gjslint']
        if not any(x in self.config.module_name
                   for x in self.MODULES_WITH_JSDOC):
            jslint_cmd.append('--nojsdoc')
        jslint_cmd.append(self.filename)

        try:
            p = Run(jslint_cmd)
            if p.status != 0:
                return p.out
        except OSError as e:
            return 'Failed to run gjslint: %s' % e
