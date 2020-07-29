from contextlib import closing
import os
import re
from tempfile import mkstemp

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
from asclib.ex import Run


class JavaFileChecker(TypificChecker):
    rulific_decision_map = {
        'copyright': True,
        'eol': True,
        'first_line_comment': True,
        'max_line_length': False,
        'no_dos_eol': True,
        'no_last_eol': True,
        'no_rcs_keywords': True,
        'no_tab_indent': True,
        'no_trailing_space': True,
    }

    typific_info = TypificCheckerInfo(comment_line_re=r'(/\*|//).*',
                                      ada_RM_spec_p=False,
                                      copyright_box_r_edge_re=None)

    # Our style file, located besides this module.
    style_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'java.xml')

    @property
    def file_type(self):
        return 'java'

    def run_external_checker(self):
        env = {
            # This sets the Java max heap size manually. By default, Java
            # allocates a value that causes a heap memory error on kwai.
            # For N909-043.
            'JAVA_ARGS': '-Xmx1024m'
        }

        # Create a properties, file, as we as can't pass -D arguments to
        # checkstyle without modifying it.
        (prop_fd, prop_filename) = mkstemp('tmp-style_checker-')

        try:
            with closing(os.fdopen(prop_fd, 'w')) as f:
                f.write('basedir=%s\n'
                        % os.path.dirname(os.path.abspath(self.filename)))

            p = Run(['checkstyle',
                     '-p', prop_filename,
                     '-c', self.style_filename,
                     '-f', 'plain',
                     self.filename],
                    env=env, ignore_environ=False)
            if p.status != 0:
                # Return the program's output minus a few useless lines.
                out = '\n'.join(
                    [line for line in p.out.splitlines()
                     if not re.match('(Starting audit|Audit done)', line)])
                return out
        except OSError as e:
            return 'Failed to run checkstyle: %s' % e

        finally:
            os.unlink(prop_filename)
