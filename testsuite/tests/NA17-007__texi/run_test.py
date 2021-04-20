def test_gnat_ugn_texi(style_checker):
    """Style check test against gnat_ugn.texi
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'gnat_ugn.texi')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_gnat_ugn_bad_copyright_texi(style_checker):
    """Style check test against gnat_ugn_bad_copyright.texi
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'gnat_ugn_bad_copyright.texi')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gnat_ugn_bad_copyright.texi:11: Copyright notice must include current year (found 1999, expected 2006)
""")
