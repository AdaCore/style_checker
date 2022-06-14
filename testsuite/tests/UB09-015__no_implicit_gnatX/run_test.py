def test_ada05_ok_1_adb(style_checker):
    """Style check test against ada05-ok-1.adb
    """
    style_checker.set_year(2021)
    p = style_checker.run_style_checker('gnat', 'a-except__zfp.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
