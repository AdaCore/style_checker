from support import *


class TestRun(TestCase):
    def test_bad_and_bad(self):
        """Style check test against bad + bad
        """
        self.set_year(2006)
        p = self.run_style_checker('hello',
                                   'ada12-no-first-line-comment.adb',
                                   'gprep_check-ko.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
""")

    def test_bad_good_bad_max_failures_1(self):
        """Style check test --max-files-with-failures=1 against
        bad + good + bad
        """
        self.set_year(2006)
        p = self.run_style_checker('--max-files-with-errors=1',
                                   'hello',
                                   'gprep_check-ko.adb',
                                   'ada12.adb',
                                   'ada12-no-first-line-comment.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
[other files with style violations were found]
""")

    def test_bad_good_bad(self):
        """Style check test against bad + good + bad
        """
        self.set_year(2006)
        p = self.run_style_checker('hello',
                                   'gprep_check-ko.adb',
                                   'ada12.adb',
                                   'ada12-no-first-line-comment.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
""")

    def test_bad_bad_good_bad(self):
        """Style check test against bad + bad + good + bad
        """
        self.set_year(2006)
        p = self.run_style_checker('hello',
                                   'gprep_check-ko.adb',
                                   'empty.adb',
                                   'ada12.adb',
                                   'ada12-no-first-line-comment.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
empty.adb:1:01: warning: file contains no compilation units
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
""")

    def test_bad_bad_good_bad_good_bad(self):
        """Style check test against bad + bad + good + bad + good + bad
        """
        self.set_year(2006)
        p = self.run_style_checker('hello',
                                   'gprep_check-ko.adb',
                                   'empty.adb',
                                   'ada12.adb',
                                   'ada12-no-first-line-comment.adb',
                                   'test1.java',
                                   'bash-ko.sh')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
empty.adb:1:01: warning: file contains no compilation units
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
[other files with style violations were found]
""")

    def test_bad_nonexistant_good_bad_good_bad(self):
        """Style check test against bad + nonexistant + good + bad + good + bad
        """
        self.set_year(2006)
        p = self.run_style_checker('hello',
                                   'gprep_check-ko.adb',
                                   'does-not-exist.adb',
                                   'ada12.adb',
                                   'ada12-no-first-line-comment.adb',
                                   'test1.java',
                                   'bash-ko.sh')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
Error: `does-not-exist.adb' is not a valid filename.
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
[other files with style violations were found]
""")

    def test_bad_bad_good_bad_good_noexistant(self):
        """Style check test against bad + bad + good + bad + good + bad
        """
        self.set_year(2006)
        p = self.run_style_checker('hello',
                                   'gprep_check-ko.adb',
                                   'empty.adb',
                                   'ada12.adb',
                                   'ada12-no-first-line-comment.adb',
                                   'test1.java',
                                   'does-not-exist.py')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
empty.adb:1:01: warning: file contains no compilation units
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
[other files with style violations were found]
""")

if __name__ == '__main__':
    runtests()
