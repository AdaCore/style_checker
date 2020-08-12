from shutil import move


def test_test_py(style_checker):
    """Run checker against test.py
    """
    move('src/test.py.rename_me', 'src/test.py')
    p = style_checker.run_style_checker('/paris.a/cvs/Dev/gps', 'src/test.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
src/test.py:2:1 'from GPS_Support import *' used; unable to detect undefined names
src/test.py:10:1 'gps_assert' may be undefined, or defined from star imports: GPS_Support
""")


def test_test_py_ok(style_checker):
    """Run checker against test.py (OK version)
    """
    move('src/test.py.rename_me-ok', 'src/test_ok.py')
    p = style_checker.run_style_checker('gps', 'src/test_ok.py')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_add_token(style_checker):
    """Run checker against add-token
    """
    p = style_checker.run_style_checker('dummy', 'src/add-token')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
src/add-token:4:19: E211 whitespace before '('
""")
