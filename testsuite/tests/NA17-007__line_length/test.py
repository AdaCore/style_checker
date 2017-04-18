from support import *

class TestRun(TestCase):
    def test_length_ko_1_adb(self):
        """Check length-ko-1.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'length-ko-1.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
length-ko-1.adb:50:80: (style) this line is too long
""")

    def test_length_ko_2_c(self):
        """Check length-ko-2.c
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'length-ko-2.c')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_misc_ok_1_c(self):
        """Check misc-ok-1.c
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'misc-ok-1.c')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
