def test_ok(style_checker):
    """Style check test against ok.mtl
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('whatever', 'ok.mtl')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_doseol(style_checker):
    """Style check test against doseol.mtl
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('whatever', 'doseol.mtl')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
doseol.mtl:1: DOS line ending is not allowed
doseol.mtl:2: DOS line ending is not allowed
doseol.mtl:3: DOS line ending is not allowed
""")


def test_no_copyright(style_checker):
    """Style check test against no-copyright.mtl
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('whatever', 'no-copyright.mtl')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
no-copyright.mtl: Copyright notice missing, must occur before line 24
""")


def test_no_last_eol(style_checker):
    """Style check test against no_last_eol.mtl
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('whatever', 'no_last_eol.mtl')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
no_last_eol.mtl:3: no newline at end of file
""")


def test_no_tab_indent(style_checker):
    """Style check test against no_tab_indent.mtl
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('whatever', 'no_tab_indent.mtl')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
no_tab_indent.mtl:3: Indentation must not use Tab characters
no_tab_indent.mtl:4: Indentation must not use Tab characters
""")
