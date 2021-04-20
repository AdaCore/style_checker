def test_good_python(style_checker):
    """Run the style checker on a python file with no error.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/check_me.txt')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
