import os


def test_a_cohama_adb(style_checker):
    """Style check test against a-cohama.adb
    """
    style_checker.set_year(2006)
    filename = os.path.join(os.getcwd(), 'a-cohama.adb')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_a_cohamb_adb(style_checker):
    """Style check test against a-cohamb.adb
    """
    filename = os.path.join(os.getcwd(), 'a-cohamb.adb')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
%(filename)s: Copyright notice missing, must occur before line 24
""" % {'filename': filename})


def test_a_cohata_ads(style_checker):
    """Style check test against a-cohata.ads
    """
    style_checker.set_year(2006)
    filename = os.path.join(os.getcwd(), 'a-cohata.ads')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_a_except_ads(style_checker):
    """Style check test against a-except.ads
    """
    style_checker.set_year(2006)
    filename = os.path.join(os.getcwd(), 'a-except.ads')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
%(filename)s:9: Copyright notice must include current year (found 2005, expected 2006)
""" % {'filename': filename})


def test_exceptions_ads(style_checker):
    """Style check test against exceptions.ads
    """
    style_checker.set_year(2006)
    filename = os.path.join(os.getcwd(), 'exceptions.ads')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
%(filename)s:9: Copyright notice must include current year (found 2005, expected 2006)
""" % {'filename': filename})


def test_a_zttest_ads(style_checker):
    """Style check test against a-zttest.ads
    """
    filename = os.path.join(os.getcwd(), 'a-zttest.ads')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_directio_ads(style_checker):
    """Style check test against directio.ads
    """
    filename = os.path.join(os.getcwd(), 'directio.ads')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_i_c_ads(style_checker):
    """Style check test against i-c.ads
    """
    filename = os.path.join(os.getcwd(), 'i-c.ads')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_s_taprop_linux_adb(style_checker):
    """Style check test s-taprop-linux.adb
    """
    style_checker.set_year(2010)
    filename = os.path.join(os.getcwd(), 's-taprop-linux.adb')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_a_unccon_ads(style_checker):
    """Style check test a-unccon.ads
    """
    filename = os.path.join(os.getcwd(), 'a-unccon.ads')
    p = style_checker.run_style_checker('gnat', filename)
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
