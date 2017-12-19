from support import *

class TestRun(TestCase):
    def test_copyright_ko_1_adb(self):
        """Style check test against copyright-ko-1.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'copyright-ko-1.adb')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
copyright-ko-1.adb:9: Copyright notice must include current year (found 2003, expected 2006)
""")

    def test_copyright_ko_2_adb(self):
        """Style check test against copyright-ko-2.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'copyright-ko-2.adb')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
copyright-ko-2.adb:1034: Copyright notice must occur before line 24
""")

    def test_copyright_ko_3_adb(self):
        """Style check test against copyright-ko-3.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'copyright-ko-3.adb')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
copyright-ko-3.adb:25: Copyright notice must occur before line 24
""")

    def test_copyright_ko_4_c(self):
        """Style check test against copyright-ko-4.c
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'copyright-ko-4.c')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
copyright-ko-4.c: Copyright notice missing, must occur before line 24
""")

    def test_copyright_ko_5_c(self):
        """Style check test against copyright-ko-5.c
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'copyright-ko-5.c')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
copyright-ko-5.c:28: Copyright notice must occur before line 24
""")

    def test_copyright_ko_6_c(self):
        """Style check test against copyright-ko-6.c
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'copyright-ko-6.c')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
copyright-ko-6.c:9: Copyright notice must include current year (found 2003, expected 2006)
""")

    def test_copyright_ko_7_adb(self):
        """Style check test against copyright-ko-7.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('trunk/gnat', 'copyright-ko-7.adb')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
copyright-ko-7.adb:2: Copyright notice has unexpected copyright holder:
      `Universidad de Cantabria, SPAIN'
Expected either of:
    - `AdaCore'
    - `Altran Praxis'
    - `Altran UK Limited'
    - `Free Software Foundation, Inc.'
    - `AdaCore, Altran Praxis'
    - `AdaCore and Altran UK Limited'
    - `AdaCore, Altran UK Limited'
    - `AdaCore and Altran UK'
    - `AdaCore, Altran UK'
""")

    def test_copyright_ok_10_h(self):
        """Style check test against copyright-ok-10.h
        """
        self.set_year(2006)
        p = self.run_style_checker('--config=binutils.yaml',
                                   'binutils', 'copyright-ok-10.h')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_copyright_ok_1_adb(self):
        """Style check test against copyright-ok-1.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'copyright-ok-1.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_copyright_ok_2_c(self):
        """Style check test against copyright-ok-2.c
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'copyright-ok-2.c')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_copyright_ok_3_adb(self):
        """Style check test against copyright-ok-3.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'copyright-ok-3.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_copyright_ok_4_c(self):
        """Style check test against copyright-ok-4.c
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'copyright-ok-4.c')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_copyright_ok_5_adb(self):
        """Style check test against copyright-ok-5.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'copyright-ok-5.adb')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
copyright-ok-5.adb:9: Copyright notice is not correctly formatted
It must look like...

    Copyright (C) 1992-2006, <copyright holder>

... where <copyright holder> can be any of:
    - `AdaCore'
    - `Altran Praxis'
    - `Altran UK Limited'
    - `Free Software Foundation, Inc.'
    - `AdaCore, Altran Praxis'
    - `AdaCore and Altran UK Limited'
    - `AdaCore, Altran UK Limited'
    - `AdaCore and Altran UK'
    - `AdaCore, Altran UK'
""")

    def test_copyright_ok_6_adb(self):
        """Style check test against copyright-ok-6.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'copyright-ok-6.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_copyright_ok_8_adb(self):
        """Style check test against copyright-ok-8.adb
        """
        self.set_year(2006)
        p = self.run_style_checker('marte', 'copyright-ok-8.adb')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_copyright_ok_9_h(self):
        """Style check test against copyright-ok-9.h
        """
        self.set_year(2006)
        p = self.run_style_checker('marte', 'copyright-ok-9.h')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_g_md5_ads(self):
        """Style check test against g-md5.ads
        """
        self.set_year(2006)
        p = self.run_style_checker('gnat', 'g-md5.ads')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
g-md5.ads: Copyright notice missing, must occur before line 24
""")


if __name__ == '__main__':
    runtests()
