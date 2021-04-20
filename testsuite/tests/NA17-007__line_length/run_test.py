def test_length_ko_1_adb(style_checker):
    """Check length-ko-1.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'length-ko-1.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
length-ko-1.adb:50:80: (style) this line is too long
""")


def test_length_ko_2_c(style_checker):
    """Check length-ko-2.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'length-ko-2.c')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_misc_ok_1_c(style_checker):
    """Check misc-ok-1.c
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'misc-ok-1.c')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
