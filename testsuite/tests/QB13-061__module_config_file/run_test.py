def test_epl_single_year_mtl(style_checker):
    """Style check test against epl_single_year.mtl
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('--config=module_config.yaml',
                                        'whatever', 'epl_single_year.mtl')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)

    # Try the same test, but without the --config file.
    # It should fail, because we no longer include the module's
    # config which allows EPL copyright notices.
    p = style_checker.run_style_checker('whatever', 'epl_single_year.mtl')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
epl_single_year.mtl:2: Copyright notice is not correctly formatted
It must look like...

    Copyright (C) 1992-2017, <copyright holder>

... where <copyright holder> can be any of:
    - `AdaCore'
    - `Altran Praxis'
    - `Altran UK Limited'
    - `Free Software Foundation, Inc.'
    - `AdaCore, Altran Praxis'
    - `AdaCore and Altran UK Limited'
    - `AdaCore, Altran UK Limited'
    - `AdaCore and Altran UK'
    - `AdaCore, Altran UK'
    - `Capgemini Engineering'
    - `AdaCore, Capgemini Engineering'
""")


def test_epl_range_mtl(style_checker):
    """Style check test against epl_range.mtl
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('--config=module_config.yaml',
                                        'whatever', 'epl_range.mtl')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)

    # Try the same test, but without the --config file.
    # It should fail, because we no longer include the module's
    # config which allows EPL copyright notices.
    p = style_checker.run_style_checker('whatever', 'epl_range.mtl')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
epl_range.mtl:2: Copyright notice is not correctly formatted
It must look like...

    Copyright (C) 1992-2017, <copyright holder>

... where <copyright holder> can be any of:
    - `AdaCore'
    - `Altran Praxis'
    - `Altran UK Limited'
    - `Free Software Foundation, Inc.'
    - `AdaCore, Altran Praxis'
    - `AdaCore and Altran UK Limited'
    - `AdaCore, Altran UK Limited'
    - `AdaCore and Altran UK'
    - `AdaCore, Altran UK'
    - `Capgemini Engineering'
    - `AdaCore, Capgemini Engineering'
""")


def test_relpath_m(style_checker):
    """Style check test against relpath.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('--config=module_config.yaml',
                                        'whatever', 'relpath.m')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
relpath.m:5: Copyright notice has unexpected copyright holder:
      `AdaCore'
Expected either of:
    - `Someone Inc'
    - `Second Holder SARL'
""")

    # Try the same test, but without the --config file.
    p = style_checker.run_style_checker('whatever', 'relpath.m')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_deep_notice(style_checker):
    """Style check test against deep_notice.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('--config=module_config.yaml',
                                        'whatever', 'deep_notice.m')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)

    # Try the same test, but without the --config file.
    p = style_checker.run_style_checker('whatever', 'deep_notice.m')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
deep_notice.m:100: Copyright notice must occur before line 24
""")


def test_notice_too_deep_m(style_checker):
    """Style check test against notice_too_deep.m
    """
    style_checker.set_year(2017)
    p = style_checker.run_style_checker('--config=module_config.yaml',
                                        'whatever', 'notice_too_deep.m')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
notice_too_deep.m:101: Copyright notice must occur before line 100
""")

    # Try the same test, but without the --config file.
    p = style_checker.run_style_checker('whatever', 'notice_too_deep.m')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
notice_too_deep.m:101: Copyright notice must occur before line 24
""")
