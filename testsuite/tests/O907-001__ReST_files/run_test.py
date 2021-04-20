def test_bad_directives(style_checker):
    """Style check test against bad_directives.rst
    """
    p = style_checker.run_style_checker('whatever', 'bad_directives.rst')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
bad_directives.rst:7: invalid directive syntax (':' should be '::')
                      .. typo-directive-no-arg:
                                              ^
bad_directives.rst:14: invalid directive syntax (':' should be '::')
                       .. typo-directive-with-args: helo smtp
                                                  ^
bad_directives.rst:23: invalid directive syntax (':' should be '::')
                       .. typo:With-Colors-not:ok:
                                                 ^
bad_directives.rst:25: invalid directive syntax (':' should be '::')
                       .. typo:with-colors-NOT:ok: args1 two
                                                 ^
""")


def test_gnat_ccg(style_checker):
    """Style check test against gnat_ccg.rst
    """
    p = style_checker.run_style_checker('gnat', 'gnat_ccg.rst')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_the_gnat_configurable_run_time_facility(style_checker):
    """Style check test against the_gnat_configurable_run_time_facility.rst
    """
    p = style_checker.run_style_checker(
        'gnat', 'the_gnat_configurable_run_time_facility.rst')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_the_gnat_compilation_model(style_checker):
    """Style check test against the_gnat_compilation_model.rst
    """
    p = style_checker.run_style_checker(
        'gnat', 'the_gnat_compilation_model.rst')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
the_gnat_compilation_model.rst:1577: invalid directive syntax (':' should be '::')
                                     .. --Comment:
                                                 ^
""")
