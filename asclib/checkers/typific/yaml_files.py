import yaml

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo


class YamlFileChecker(TypificChecker):
    rulific_decision_map = {
        'copyright': False,
        'eol': False,
        'first_line_comment': False,
        'max_line_length': False,
        'no_dos_eol': False,
        'no_last_eol': False,
        'no_rcs_keywords': False,
        'no_tab_indent': False,
        'no_trailing_space': False,
        }

    typific_info = TypificCheckerInfo(comment_line_re=None,
                                      ada_RM_spec_p=False,
                                      copyright_box_r_edge_re=None)

    @property
    def file_type(self):
        return 'YaML file'

    def run_external_checker(self):
        try:
            with open(self.filename, 'rb') as fd:
                yaml.load(fd)
        except yaml.YAMLError as exc:
            return 'Error: %s: %s' % (self.filename, str(exc))
