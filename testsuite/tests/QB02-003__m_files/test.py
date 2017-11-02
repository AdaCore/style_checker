from support import *

class TestRun(TestCase):
    def test_ok(self):
        """Style check test against ok.m
        """
        self.set_year(2017)
        p = self.run_style_checker('whatever', 'ok.m')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_rcs_rev(self):
        """Style check test against ok-rcs-rev.m
        """
        self.set_year(2017)
        p = self.run_style_checker('whatever', 'ok-rcs-rev.m')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_nok_dos(self):
        """Style check test against nok-dos.m
        """
        self.set_year(2017)
        p = self.run_style_checker('whatever', 'nok-dos.m')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
nok-dos.m:36: DOS line ending is not allowed
nok-dos.m:36: inconsistent newline: cr+lf [dos] (the previous line used lf [unix])
""")

    def test_nok_tab(self):
        """Style check test against nok-tab.m
        """
        self.set_year(2017)
        p = self.run_style_checker('whatever', 'nok-tab.m')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
nok-tab.m:36: Indentation must not use Tab characters
nok-tab.m:37: Indentation must not use Tab characters
""")

    def test_nok_trailing(self):
        """Style check test against nok-trailing.m
        """
        self.set_year(2017)
        p = self.run_style_checker('whatever', 'nok-trailing.m')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
nok-trailing.m:15: Trailing spaces are not allowed
""")

    def test_nok_copyright(self):
        """Style check test against nok-copyright.m
        """
        self.set_year(2017)
        p = self.run_style_checker('whatever', 'nok-copyright.m')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
nok-copyright.m: Copyright notice missing, must occur before line 24
""")


if __name__ == '__main__':
    runtests()
