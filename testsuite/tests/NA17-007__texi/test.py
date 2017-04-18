from support import *

class TestRun(TestCase):
    def test_gnat_ugn_texi(self):
        """Style check test against gnat_ugn.texi
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'gnat_ugn.texi')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_gnat_ugn_bad_copyright_texi(self):
        """Style check test against gnat_ugn_bad_copyright.texi
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'gnat_ugn_bad_copyright.texi')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
gnat_ugn_bad_copyright.texi:11: Copyright notice must include current year (found 1999, expected 2006)
""")


if __name__ == '__main__':
    runtests()
