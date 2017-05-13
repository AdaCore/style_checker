from support import *

class TestRun(TestCase):
    def test_trailing_ko_1_adb(self):
        """Style check test against trailing-ko-1.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'trailing-ko-1.adb')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
trailing-ko-1.adb:1511:78: (style) trailing spaces not permitted
""")

    def test_trailing_ko_2_c(self):
        """Style check test against trailing-ko-2.c
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'trailing-ko-2.c')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
trailing-ko-2.c:173: Trailing spaces are not allowed
trailing-ko-2.c:9: Copyright notice must include current year (found 2005, expected 2006)
""")

    def test_trailing_tab(self):
        """Style check test against trailing-tab.c
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'trailing-tab.c')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
trailing-tab.c:30: Trailing spaces are not allowed
""")


if __name__ == '__main__':
    runtests()
