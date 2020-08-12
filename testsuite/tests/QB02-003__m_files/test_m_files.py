def test_ok(style_checker):
    """Style check test against ok.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('whatever', 'ok.m')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_rcs_rev(style_checker):
    """Style check test against ok-rcs-rev.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('whatever', 'ok-rcs-rev.m')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_iqgen_write_log(style_checker):
    """Style check test against iqgen_write_log.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('whatever', 'iqgen_write_log.m')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_nok_dos(style_checker):
    """Style check test against nok-dos.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('whatever', 'nok-dos.m')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
nok-dos.m:36: DOS line ending is not allowed
nok-dos.m:36: inconsistent newline: cr+lf [dos] (the previous line used lf [unix])
""")


def test_nok_tab(style_checker):
    """Style check test against nok-tab.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('whatever', 'nok-tab.m')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
nok-tab.m:36: Indentation must not use Tab characters
nok-tab.m:37: Indentation must not use Tab characters
""")


def test_nok_trailing(style_checker):
    """Style check test against nok-trailing.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('whatever', 'nok-trailing.m')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
nok-trailing.m:15: Trailing spaces are not allowed
""")


def test_nok_copyright(style_checker):
    """Style check test against nok-copyright.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('whatever', 'nok-copyright.m')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
nok-copyright.m: Copyright notice missing, must occur before line 24
""")
