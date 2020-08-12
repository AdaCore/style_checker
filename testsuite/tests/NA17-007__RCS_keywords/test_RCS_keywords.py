def test_rev_ko_1_c(style_checker):
    """Check rev-ko-1.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'rev-ko-1.c')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
rev-ko-1.c:10: RCS Revision keyword not allowed
""")


def test_rev_ko_2_adb(style_checker):
    """Check rev-ko-2.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'rev-ko-2.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
rev-ko-2.adb:10: RCS Revision keyword not allowed
""")
