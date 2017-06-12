from support import *

class TestRun(TestCase):
    def test_a_cohama_adb(self):
        """Style check test against a-cohama.adb
        """
        self.set_year(2006)
        filename = os.path.join(os.getcwd(), 'a-cohama.adb')
        p = self.run_style_checker('gnat', filename)
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_a_cohamb_adb(self):
        """Style check test against a-cohamb.adb
        """
        filename = os.path.join(os.getcwd(), 'a-cohamb.adb')
        p = self.run_style_checker('gnat', filename)
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
%(filename)s: Copyright notice missing, must occur before line 24
""" % {'filename': filename})

    def test_a_cohata_ads(self):
        """Style check test against a-cohata.ads
        """
        self.set_year(2006)
        filename = os.path.join(os.getcwd(), 'a-cohata.ads')
        p = self.run_style_checker('gnat', filename)
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_a_except_ads(self):
        """Style check test against a-except.ads
        """
        self.set_year(2006)
        filename = os.path.join(os.getcwd(), 'a-except.ads')
        p = self.run_style_checker('gnat', filename)
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
%(filename)s:9: Copyright notice must include current year (found 2005, expected 2006)
""" % {'filename': filename})

    def test_exceptions_ads(self):
        """Style check test against exceptions.ads
        """
        self.set_year(2006)
        filename = os.path.join(os.getcwd(), 'exceptions.ads')
        p = self.run_style_checker('gnat', filename)
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
%(filename)s:9: Copyright notice must include current year (found 2005, expected 2006)
""" % {'filename': filename})

    def test_a_zttest_ads(self):
        """Style check test against a-zttest.ads
        """
        filename = os.path.join(os.getcwd(), 'a-zttest.ads')
        p = self.run_style_checker('gnat', filename)
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_directio_ads(self):
        """Style check test against directio.ads
        """
        filename = os.path.join(os.getcwd(), 'directio.ads')
        p = self.run_style_checker('gnat', filename)
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_i_c_ads(self):
        """Style check test against i-c.ads
        """
        filename = os.path.join(os.getcwd(), 'i-c.ads')
        p = self.run_style_checker('gnat', filename)
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_s_taprop_linux_adb(self):
        """Style check test s-taprop-linux.adb
        """
        self.set_year(2010)
        filename = os.path.join(os.getcwd(), 's-taprop-linux.adb')
        p = self.run_style_checker('gnat', filename)
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_a_unccon_ads(self):
        """Style check test a-unccon.ads
        """
        filename = os.path.join(os.getcwd(), 'a-unccon.ads')
        p = self.run_style_checker('gnat', filename)
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)



if __name__ == '__main__':
    runtests()
