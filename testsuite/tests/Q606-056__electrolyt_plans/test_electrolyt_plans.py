def test_linux_plan(style_checker):
    """Run checker against linux.plan
    """
    p = style_checker.run_style_checker('electrolyt', 'linux.plan')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_linux_ko_plan(style_checker):
    """Run checker against linux-ko.plan
    """
    p = style_checker.run_style_checker('electrolyt', 'linux-ko.plan')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
linux-ko.plan:11:24: E251 unexpected spaces around keyword / parameter equals
linux-ko.plan:11:26: E251 unexpected spaces around keyword / parameter equals
linux-ko.plan:12:15: E211 whitespace before '('
""")
