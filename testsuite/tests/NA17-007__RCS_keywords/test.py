from support import *

class TestRun(TestCase):
    def test_rev_ko_1_c(self):
        """Check rev-ko-1.c
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'rev-ko-1.c')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
rev-ko-1.c:10: RCS Revision keyword not allowed
""")

    def test_rev_ko_2_adb(self):
        """Check rev-ko-2.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'rev-ko-2.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
rev-ko-2.adb:10: RCS Revision keyword not allowed
""")


if __name__ == '__main__':
    runtests()
