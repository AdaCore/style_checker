import os


def test_ada05_ok_1_adb(style_checker):
    """Style check test against ada05-ok-1.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('/paris.a/cvs/Dev/toto', 'ada05-ok-1.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_ada12_adb(style_checker):
    """Style check test against ada12.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/toto', 'ada12.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_gprep_check_ko_adb(style_checker):
    """Style check test against ada12.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'gprep_check-ko.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:2:01: (style) reserved words must be all lower case
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
""")


def test_hang_ok_1_ads(style_checker):
    """Style check test against hang-ok-1.ads
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'hang-ok-1.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_hang_ok_2_ads(style_checker):
    """Style check test against hang-ok-2.ads
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'hang-ok-2.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_ipstack_adb(style_checker):
    """Style check test against ipstack.adb
    """
    style_checker.set_year(2012)
    p = style_checker.run_style_checker('trunk/ipstack', 'ipstack.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_switch_c_adb(style_checker):
    """Style check test against switch-c.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/ipstack', 'switch-c.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_ada12_no_first_line_comment_adb(style_checker):
    """Style check test against ada12-no-first-line-comment.adb
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/toto',
                                        'ada12-no-first-line-comment.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
""")


def test_ada_gnatx(style_checker):
    """Style check Ada unit in repository that uses the gnatx config
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('java', 'switch-c.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_ada_gnat95_ok(style_checker):
    """Style check Ada unit with gnat95 without any violation.
    """
    p = style_checker.run_style_checker(
        '--system-config',
        os.path.join(os.getcwd(), 'gnat95_config', 'alt_config.yaml'),
        'examples', 'gnat95_config/pck.ads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_ada_gnat95_with_ada2005_violation(style_checker):
    """Style check with gnat95 of Ada unit using Ada 2005 construct
    """
    p = style_checker.run_style_checker(
        '--system-config',
        os.path.join(os.getcwd(), 'gnat95_config', 'alt_config.yaml'),
        'examples', 'gnat95_config/has_05.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
has_05.adb:8:27: string expression in raise is an Ada 2005 extension
has_05.adb:8:27: unit must be compiled with -gnat05 switch
""")


def test_ada_gnat05(style_checker):
    """Style check Ada unit with gnat05
    """
    p = style_checker.run_style_checker(
        '--system-config',
        os.path.join(os.getcwd(), 'gnat05_config', 'alt_config.yaml'),
        'examples', 'gnat05_config/pck.ads')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
pck.ads:1:04: (style) space required
pck.ads:2:04: (style) space required
pck.ads:3:04: (style) space required
""")


def test_s_taprop__linux_adb(style_checker):
    """Make sure we check s-taprop__linux.adb with -gnat12
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('gnat', 'libgnarl/s-taprop__linux.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_ada_2005_ok_in_gnat_compiler_core(style_checker):
    """Verify that COMPILER_CORE files can use Ada 2005 constructs
    """
    style_checker.set_year(2020)
    p = style_checker.run_style_checker('gnat', 'bindo.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_ada_2012_ok_in_gnat_compiler_core(style_checker):
    """Verify that COMPILER_CORE files can use Ada 2012 constructs
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnat', 'ada12.adb')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
