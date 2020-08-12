def test_xzutils_anod(style_checker):
    """Run checker against xzutils.anod
    """
    p = style_checker.run_style_checker('anod', 'xzutils.anod')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_xzutils_ko_pep8_anod(style_checker):
    """Run checker against xzutils-ko-pep8.anod
    """
    p = style_checker.run_style_checker('anod', 'xzutils-ko-pep8.anod')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
xzutils-ko-pep8.anod:3:1: E302 expected 2 blank lines, found 1
""")


def test_xzutils_ko_pyflakes_anod(style_checker):
    """Run checker against xzutils-ko-pyflakes.anod
    """
    p = style_checker.run_style_checker('anod', 'xzutils-ko-pyflakes.anod')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
xzutils-ko-pyflakes.anod:1:15 undefined name 'spec'
""")
