def test_test1(style_checker):
    """Style check test against test1.java
    """
    p = style_checker.run_style_checker('/paris.a/cvs/Dev/gnatbench',
                               'test1.java')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
test1.java:1: First line must start with a comment (regexp: (/\*|//).*)
test1.java: Copyright notice missing, must occur before line 24
""")


def test_test1_star_import(style_checker):
    """Style check test against test1-start-import.java

    This is actually the original version of test1.java, which
    apparently used to pass the external-checker check but no
    longer does, because the configuration we now use explicitly
    request that we flag .* import as errors.
    """
    p = style_checker.run_style_checker('gnatbench',
                               'test1-start-import.java')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
[warning] /usr/bin/checkstyle: Unable to locate commons-cli in /usr/share/java
[ERROR] test1-start-import.java:1: Using the '.*' form of import should be avoided - java.io.*. [AvoidStarImport]
Checkstyle ends with 1 errors.
""")


def test_test2(style_checker):
    """Style check test against test2.java

    Note that we removed the import from the original test (from
    the days the style checker was cvs_check, a part of the infosys
    project), because that import uses the .* form, which is now
    explicitly forbidden.
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnatbench', 'test2.java')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_test3(style_checker):
    """Style check test against test3.java

    Note that we removed the import from the original test (from
    the days the style checker was cvs_check, a part of the infosys
    project), because that import uses the .* form, which is now
    explicitly forbidden.
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnatbench', 'test3.java')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_GNAT_libc(style_checker):
    """Style check test against GNAT_libc.java

    Note that we removed the import from the original test (from
    the days the style checker was cvs_check, a part of the infosys
    project), because that import uses the .* form, which is now
    explicitly forbidden.
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnatbench', 'GNAT_libc.java')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
