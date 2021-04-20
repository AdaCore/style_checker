def test_trailing_ko_1_adb(style_checker):
    """Style check test against trailing-ko-1.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'trailing-ko-1.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
trailing-ko-1.adb:1511:78: (style) trailing spaces not permitted
""")


def test_trailing_ko_2_c(style_checker):
    """Style check test against trailing-ko-2.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'trailing-ko-2.c')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
trailing-ko-2.c:173: Trailing spaces are not allowed
trailing-ko-2.c:9: Copyright notice must include current year (found 2005, expected 2006)
""")


def test_trailing_tab(style_checker):
    """Style check test against trailing-tab.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'trailing-tab.c')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
trailing-tab.c:30: Trailing spaces are not allowed
""")
