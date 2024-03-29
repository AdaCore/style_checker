def test_doseol_ko_1_adb(style_checker):
    """Check doseol-ko-1.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'doseol-ko-1.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
doseol-ko-1.adb:1: DOS line ending is not allowed
doseol-ko-1.adb:2: DOS line ending is not allowed
doseol-ko-1.adb:3: DOS line ending is not allowed [similar errors no longer shown]
doseol-ko-1.adb:9: Copyright notice must include current year (found 2005, expected 2006)
""")

def test_doseol_ko_2_c(style_checker):
    """Check doseol-ko-2.c
    """
    style_checker.set_year(2005)
    p = style_checker.run_style_checker('gnat', 'doseol-ko-2.c')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
doseol-ko-2.c:1: DOS line ending is not allowed
doseol-ko-2.c:2: DOS line ending is not allowed
doseol-ko-2.c:3: DOS line ending is not allowed [similar errors no longer shown]
""")

def test_doseol_ko_3_adb(style_checker):
    """Check doseol-ko-3.adb
    """
    style_checker.set_year(2005)
    p = style_checker.run_style_checker('gnat', 'doseol-ko-3.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
doseol-ko-3.adb:26:01: (style) multiple blank lines
""")

def test_doseol_ko_4_c(style_checker):
    """Check doseol-ko-4.c
    """
    style_checker.set_year(2005)
    p = style_checker.run_style_checker('gnat', 'doseol-ko-4.c')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
doseol-ko-4.c:27: DOS line ending is not allowed
doseol-ko-4.c:27: inconsistent newline: cr+lf [dos] (the previous line used lf [unix])
doseol-ko-4.c:28: DOS line ending is not allowed
doseol-ko-4.c:29: DOS line ending is not allowed [similar errors no longer shown]
""")

def test_doseol_ko_5_adb(style_checker):
    """Check doseol-ko-5.adb
    """
    style_checker.set_year(2005)
    p = style_checker.run_style_checker('gnat', 'doseol-ko-5.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
doseol-ko-5.adb:1612:37: error: missing string quote
doseol-ko-5.adb:1613:02: error: missing string quote
""")

def test_doseol_ok_1_sh(style_checker):
    """Check doseol-ok-1.sh
    """
    p = style_checker.run_style_checker('gnat', 'doseol-ok-1.sh')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
