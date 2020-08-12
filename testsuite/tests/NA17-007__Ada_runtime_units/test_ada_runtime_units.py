def test_a_cohama_adb(style_checker):
    """Style check test against a-cohama.adb."""
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'a-cohama.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_a_cohamb_adb(style_checker):
    """Style check test against a-cohamb.adb."""
    p = style_checker.run_style_checker('trunk/gnat', 'a-cohamb.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
a-cohamb.adb: Copyright notice missing, must occur before line 24
""")


def test_a_cohata_ads(style_checker):
    """Style check test against a-cohata.ads."""
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'a-cohata.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_a_except_ads(style_checker):
    """Style check test against a-except.ads."""
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'a-except.ads')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
a-except.ads:9: Copyright notice must include current year (found 2005, expected 2006)
""")


def test_exceptions_ads(style_checker):
    """Style check test against exceptions.ads."""
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'exceptions.ads')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
exceptions.ads:9: Copyright notice must include current year (found 2005, expected 2006)
""")


def test_a_zttest_ads(style_checker):
    """Style check test against a-zttest.ads
    """
    p = style_checker.run_style_checker('trunk/gnat', 'a-zttest.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_directio_ads(style_checker):
    """Style check test against directio.ads
    """
    p = style_checker.run_style_checker('trunk/gnat', 'directio.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_i_c_ads(style_checker):
    """Style check test against i-c.ads
    """
    p = style_checker.run_style_checker('trunk/gnat', 'i-c.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_s_taprop_linux_adb(style_checker):
    """Style check test s-taprop-linux.adb
    """
    style_checker.set_year(2010)
    p = style_checker.run_style_checker('trunk/gnat', 's-taprop-linux.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
