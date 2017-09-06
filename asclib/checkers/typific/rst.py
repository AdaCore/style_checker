import re

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo


class RstFileChecker(TypificChecker):
    rulific_decision_map = {
        'copyright': False,
        'eol': True,
        'first_line_comment': False,
        'max_line_length': False,
        'no_dos_eol': True,
        'no_last_eol': True,
        'no_rcs_keywords': False,
        'no_trailing_space': False,
        }

    typific_info = TypificCheckerInfo(comment_line_re=None,
                                      ada_RM_spec_p=False,
                                      copyright_box_r_edge_re=None)

    @property
    def file_type(self):
        return 'ReST file'

    def run_external_checker(self):

        # Check that user user didn't forget the second colon in
        # what looks like a directive, but isn't. For instance...
        #
        #    .. note: someting
        #
        # ... which looks like the user actually meant to be:
        #
        #    .. note:: someting
        #
        # The syntax for directives is the sequence of:
        #    - '..'
        #    - the directive type
        #      (case-insentive words, which are alphanumerics, plus
        #       ISOLATED internal hyphens, underscores, plus signs,
        #       colons, and periods; no whitespace)
        #    - '::'
        #    - arguments (optional)
        #
        # Allowing isolated colons in the directive type means that
        # we cannot simply use a single colon as the delimiter for
        # the directive type. So what we do is the following: For
        # lines that start with '..' and a space, extract everything
        # after it until the last colon on the line. If somewhere in
        # there, we find two colons, then that's the boundary of
        # the directive type, and the user properly used two colons,
        # so all good. If we don't find any occurence of '::', then
        # the user likely made a typo.
        directive_matcher = re.compile(
            r'^\.\.\s+([-_+:.a-zA-Z0-9]+:)', re.IGNORECASE)

        errors = []
        with open(self.filename) as f:
            for line_no, line in enumerate(f, 1):
                m = directive_matcher.match(line)
                if m is None:
                    # This line does not have a directive
                    continue
                if m.group(1).startswith('_'):
                    # This is a hyperlink target, not a directive.
                    continue
                if m.group(1).lower() == '--comment:':
                    # Convention at AdaCore for provinding comments.
                    continue
                if '::' in m.group(1):
                    # This line has a directive, and the syntax looks correct.
                    continue
                # It looks like this line has a directive, and that
                # the user may have made a typo.
                loc = "%s:%d" % (self.filename, line_no)
                errors.extend([
                    "%s: invalid directive syntax (':' should be '::')" % loc,
                    "%s  %s" % (' ' * len(loc), line.rstrip()),
                    "%s  %s" % (' ' * len(loc),
                                ' ' * len(m.group(0)[:-1]) + '^')])

        if errors:
            return '\n'.join(errors)
