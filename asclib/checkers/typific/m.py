from asclib.checkers.typific import TypificChecker, TypificCheckerInfo


class MFileChecker(TypificChecker):
    rulific_decision_map = {
        "bidi": True,
        "copyright": True,
        "eol": True,
        "first_line_comment": False,
        "max_line_length": False,
        "no_dos_eol": True,
        "no_last_eol": True,
        "no_rcs_keywords": False,
        "no_tab_indent": True,
        "no_trailing_space": True,
    }

    typific_info = TypificCheckerInfo(
        comment_line_re=None, ada_RM_spec_p=False, copyright_box_r_edge_re="%"
    )

    @property
    def file_type(self):
        # This Typific checker was created mostly for matlab files,
        # but as it happens, right now, the same extension is also
        # used for other types of files. Since the checking we are
        # doing for it is fairly generic, just use a generic name
        # for the file type as well.
        return ".m files (matlab, Obj-C, mathematica...)"

    def run_external_checker(self):
        # Nothing to do.
        pass
