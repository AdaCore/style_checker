from support import *

class TestRun(TestCase):
    def test_a_cohama_adb(self):
        """Style check test against a-cohama.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'a-cohama.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_a_cohamb_adb(self):
        """Style check test against a-cohamb.adb
        """
        p = self.run_style_checker('trunk/gnat', 'a-cohamb.adb')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
a-cohamb.adb: Copyright notice missing, must occur before line 24
""")

    def test_a_cohata_ads(self):
        """Style check test against a-cohata.ads
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'a-cohata.ads')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_a_except_ads(self):
        """Style check test against a-except.ads
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'a-except.ads')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
a-except.ads:9: Copyright notice must include current year (found 2005, expected 2006)
""")

    def test_exceptions_ads(self):
        """Style check test against exceptions.ads
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'exceptions.ads')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
exceptions.ads:9: Copyright notice must include current year (found 2005, expected 2006)
""")

    def test_a_zttest_ads(self):
        """Style check test against a-zttest.ads
        """
        p = self.run_style_checker('trunk/gnat', 'a-zttest.ads')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_directio_ads(self):
        """Style check test against directio.ads
        """
        p = self.run_style_checker('trunk/gnat', 'directio.ads')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_i_c_ads(self):
        """Style check test against i-c.ads
        """
        p = self.run_style_checker('trunk/gnat', 'i-c.ads')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_s_taprop_linux_adb(self):
        """Style check test s-taprop-linux.adb
        """
        self.set_year(2010)
        p = self.run_style_checker('trunk/gnat', 's-taprop-linux.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
