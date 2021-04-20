def test_copyright_ko_1_adb(style_checker):
    """Style check test against copyright-ko-1.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'copyright-ko-1.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
copyright-ko-1.adb:9: Copyright notice must include current year (found 2003, expected 2006)
""")


def test_copyright_ko_2_adb(style_checker):
    """Style check test against copyright-ko-2.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'copyright-ko-2.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
copyright-ko-2.adb:1034: Copyright notice must occur before line 24
""")


def test_copyright_ko_3_adb(style_checker):
    """Style check test against copyright-ko-3.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'copyright-ko-3.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
copyright-ko-3.adb:25: Copyright notice must occur before line 24
""")


def test_copyright_ko_4_c(style_checker):
    """Style check test against copyright-ko-4.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'copyright-ko-4.c')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
copyright-ko-4.c: Copyright notice missing, must occur before line 24
""")


def test_copyright_ko_5_c(style_checker):
    """Style check test against copyright-ko-5.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'copyright-ko-5.c')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
copyright-ko-5.c:28: Copyright notice must occur before line 24
""")


def test_copyright_ko_6_c(style_checker):
    """Style check test against copyright-ko-6.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'copyright-ko-6.c')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
copyright-ko-6.c:9: Copyright notice must include current year (found 2003, expected 2006)
""")


def test_copyright_ko_7_adb(style_checker):
    """Style check test against copyright-ko-7.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'copyright-ko-7.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
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


def test_copyright_ok_10_h(style_checker):
    """Style check test against copyright-ok-10.h
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('--config=binutils.yaml',
                                        'binutils', 'copyright-ok-10.h')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_copyright_ok_1_adb(style_checker):
    """Style check test against copyright-ok-1.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'copyright-ok-1.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_copyright_ok_2_c(style_checker):
    """Style check test against copyright-ok-2.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'copyright-ok-2.c')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_copyright_ok_3_adb(style_checker):
    """Style check test against copyright-ok-3.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'copyright-ok-3.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_copyright_ok_4_c(style_checker):
    """Style check test against copyright-ok-4.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'copyright-ok-4.c')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_copyright_ok_5_adb(style_checker):
    """Style check test against copyright-ok-5.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'copyright-ok-5.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
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


def test_copyright_ok_6_adb(style_checker):
    """Style check test against copyright-ok-6.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'copyright-ok-6.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_copyright_ok_8_adb(style_checker):
    """Style check test against copyright-ok-8.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('--config=marte.yaml',
                                        'marte', 'copyright-ok-8.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_copyright_ok_9_h(style_checker):
    """Style check test against copyright-ok-9.h
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('--config=marte.yaml',
                                        'marte', 'copyright-ok-9.h')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_g_md5_ads(style_checker):
    """Style check test against g-md5.ads
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'g-md5.ads')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
g-md5.ads: Copyright notice missing, must occur before line 24
""")
