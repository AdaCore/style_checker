def test_good_python(style_checker):
    """Run the style checker on a python file with no error.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/good.py')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_good_python_with_verbose(style_checker):
    """Verbose run on a python file with no error.

    This is the same as test_good_python, but running the style_checker
    in verbose mode (mostly for coverage)....
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/good.py', '-v')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
Checking style of `src/good.py' (Python script)
""")


def test_bad_python(style_checker):
    """Run the style checker on a python file with a style violation.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/bad.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
src/bad.py:4:13: E211 whitespace before '('
""")


def test_nonexistant_python(style_checker):
    """Run the style checker on a python file with no error.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/hello.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
Error: `src/hello.py' is not a valid filename.
""")
