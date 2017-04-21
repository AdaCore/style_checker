from support import *

class TestRun(TestCase):
    def test_ada05_ok_1_adb(self):
        """Style check test against ada05-ok-1.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('/paris.a/cvs/Dev/toto', 'ada05-ok-1.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_ada12_adb(self):
        """Style check test against ada12.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/toto', 'ada12.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_gprep_check_ko_adb(self):
        """Style check test against ada12.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'gprep_check-ko.adb')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
""")

    def test_hang_ok_1_ads(self):
        """Style check test against hang-ok-1.ads
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'hang-ok-1.ads')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_hang_ok_2_ads(self):
        """Style check test against hang-ok-2.ads
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'hang-ok-2.ads')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_ipstack_adb(self):
        """Style check test against ipstack.adb
        """
        self.set_year(2012)
        p = self.run_style_checker('trunk/ipstack', 'ipstack.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_switch_c_adb(self):
        """Style check test against switch-c.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/ipstack', 'switch-c.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
