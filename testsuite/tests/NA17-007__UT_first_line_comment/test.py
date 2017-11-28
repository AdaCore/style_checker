from support import *

class TestRun(TestCase):
    def test_comment_re_with_no_end_dollar(self):
        """test first_line_comment with regexp not ending with '$'.

        At the moment, there is no language where that is the case,
        so we need to resort to Unit Testing.
        """
        self.enable_unit_test()

        from asclib import get_system_config_default_filename
        from asclib.config import Config
        from asclib.checkers.typific.c import CFileChecker
        from asclib.checkers import FileCheckerError

        CFileChecker.typific_info.comment_line_re = r'/\**'
        CFileChecker.rulific_decision_map['first_line_comment'] = True
        config = Config(get_system_config_default_filename(),
                        'supermod', 2006)
        c_checker = CFileChecker('hello-no-first-line-comment.c', config)

        with self.assertRaises(FileCheckerError) as cm:
            c_checker.check_file()
        expected_output = '''\
hello-no-first-line-comment.c:1: First line must start with a comment (regexp: /\**)'''
        self.assertOutputEqual(expected_output, str(cm.exception))


if __name__ == '__main__':
    runtests()
