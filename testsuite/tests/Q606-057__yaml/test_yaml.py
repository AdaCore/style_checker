def test_config_yaml(style_checker):
    """Run checker against config.yaml
    """
    p = style_checker.run_style_checker('electrolyt', 'config.yaml')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_config_ko_yaml(style_checker):
    """Run checker against config_ko.yaml
    """
    p = style_checker.run_style_checker('electrolyt', 'config_ko.yaml')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
Error: config_ko.yaml: while parsing a flow sequence
  in "config_ko.yaml", line 10, column 13
expected ',' or ']', but got '<scalar>'
  in "config_ko.yaml", line 12, column 5
""")
