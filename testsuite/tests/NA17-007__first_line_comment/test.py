from support import *


class TestRun(TestCase):
    def test_comment_ko_1_adb(self):
        """First line is not a comment
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'comment-ko-1.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
comment-ko-1.adb:1: First line must be comment markers only.
""")


if __name__ == '__main__':
    runtests()
