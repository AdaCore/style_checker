def test_f2020_adb(style_checker):
    """Style check test against f2020.adb."""
    # Check a file that uses Ada 2022 features. This should now
    # be accepted by default (see U618-006).
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('repo_name', 'f2020.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)

    # Do the same test as above, but saying that the file is
    # part of the gnat repository. In the gnat repository,
    # f2020.adb would be considered a COMPILER_CORE file, and
    # thus would be checked for Ada 2012 compatibilty.

    p = style_checker.run_style_checker('gnat', 'f2020.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
f2020.adb:13:22: error: target name is an Ada 2022 feature
f2020.adb:13:22: error: unit must be compiled with -gnat2022 switch
""")


def test_f2020_adb_with_gnat2020_config(style_checker):
    """Style check f2020.adb with gnat2020 config."""
    style_checker.set_year(2006)
    p = style_checker.run_style_checker(
        '--config', 'gnat2020_config.yaml', 'repo_name', 'f2020.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)

    # Do the same test as above, but saying that the file is
    # part of the gnat repository. In the gnat repository,
    # f2020.adb would be considered a COMPILER_CORE file, and
    # thus would be checked for Ada 2012 compatibilty, regardless
    # of the configuration file saying we should allow Ada 2020.

    p = style_checker.run_style_checker(
        '--config', 'gnat2020_config.yaml', 'gnat', 'f2020.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
f2020.adb:13:22: error: target name is an Ada 2022 feature
f2020.adb:13:22: error: unit must be compiled with -gnat2022 switch
""")
