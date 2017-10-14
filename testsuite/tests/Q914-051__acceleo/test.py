from support import *

class TestRun(TestCase):
    def test_ok(self):
        """Style check test against ok.mtl
        """
        self.set_year(2006)
        p = self.run_style_checker('whatever', 'ok.mtl')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_doseol(self):
        """Style check test against doseol.mtl
        """
        self.set_year(2006)
        p = self.run_style_checker('whatever', 'doseol.mtl')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
doseol.mtl:1: DOS line ending is not allowed
doseol.mtl:2: DOS line ending is not allowed
doseol.mtl:3: DOS line ending is not allowed
""")

    def test_no_copyright(self):
        """Style check test against no-copyright.mtl
        """
        self.set_year(2006)
        p = self.run_style_checker('whatever', 'no-copyright.mtl')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
no-copyright.mtl: Copyright notice missing, must occur before line 24
""")

    def test_no_last_eol(self):
        """Style check test against no_last_eol.mtl
        """
        self.set_year(2006)
        p = self.run_style_checker('whatever', 'no_last_eol.mtl')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
no_last_eol.mtl:3: no newline at end of file
""")

    def test_no_tab_indent(self):
        """Style check test against no_tab_indent.mtl
        """
        self.set_year(2006)
        p = self.run_style_checker('whatever', 'no_tab_indent.mtl')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
no_tab_indent.mtl:3: Indentation must not use Tab characters
no_tab_indent.mtl:4: Indentation must not use Tab characters
""")


if __name__ == '__main__':
    runtests()
