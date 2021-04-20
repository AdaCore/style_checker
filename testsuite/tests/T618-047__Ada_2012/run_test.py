def test_pck_2012_adb(style_checker):
    """Style check test against pck_2012.adb."""
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('repo_name', 'pck_2012.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_pck_2012_adb_with_alt_config_forcing_gnat2012(style_checker):
    """Style check test against pck_2012.adb with gnat12 config option."""
    style_checker.set_year(2006)
    p = style_checker.run_style_checker(
       '--config', 'gnat2012_config.yaml', 'repo_name', 'pck_2012.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
