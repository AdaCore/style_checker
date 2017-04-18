from support import *

class TestRun(TestCase):
    def test_doseol_ko_1_adb(self):
        """Check doseol-ko-1.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'doseol-ko-1.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
doseol-ko-1.adb:1: DOS line ending is not allowed
doseol-ko-1.adb:2: DOS line ending is not allowed
doseol-ko-1.adb:3: DOS line ending is not allowed [similar errors no longer shown]
doseol-ko-1.adb:9: Copyright notice must include current year (found 2005, expected 2006)
""")

    def test_doseol_ko_2_c(self):
        """Check doseol-ko-2.c
        """
        self.set_year(2005)
        p = self.run_style_checker('gnat', 'doseol-ko-2.c')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
doseol-ko-2.c:1: DOS line ending is not allowed
doseol-ko-2.c:2: DOS line ending is not allowed
doseol-ko-2.c:3: DOS line ending is not allowed [similar errors no longer shown]
""")

    def test_doseol_ko_3_adb(self):
        """Check doseol-ko-3.adb
        """
        self.set_year(2005)
        p = self.run_style_checker('gnat', 'doseol-ko-3.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
doseol-ko-3.adb:26:01: (style) multiple blank lines
""")

    def test_doseol_ko_4_c(self):
        """Check doseol-ko-4.c
        """
        self.set_year(2005)
        p = self.run_style_checker('gnat', 'doseol-ko-4.c')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
doseol-ko-4.c:27: DOS line ending is not allowed
doseol-ko-4.c:27: inconsistent newline: cr+lf [dos] (the previous line used lf [unix])
doseol-ko-4.c:28: DOS line ending is not allowed
doseol-ko-4.c:29: DOS line ending is not allowed [similar errors no longer shown]
""")

    def test_doseol_ko_5_adb(self):
        """Check doseol-ko-5.adb
        """
        self.set_year(2005)
        p = self.run_style_checker('gnat', 'doseol-ko-5.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
doseol-ko-5.adb:1612:37: missing string quote
doseol-ko-5.adb:1613:02: missing string quote
""")

    def test_doseol_ok_1_sh(self):
        """Check doseol-ok-1.sh
        """
        p = self.run_style_checker('gnat', 'doseol-ok-1.sh')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
