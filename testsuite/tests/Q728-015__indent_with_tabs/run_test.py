def test_test2(style_checker):
    """Style check test against test2.java
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnatbench', 'test2.java')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
test2.java:10: Trailing spaces are not allowed
test2.java:11: Indentation must not use Tab characters
test2.java:12: Indentation must not use Tab characters
test2.java:13: Indentation must not use Tab characters
""")


def test_test3(style_checker):
    """Style check test against test3.java
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnatbench', 'test3.java')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
test3.java:8: Indentation must not use Tab characters
test3.java:9: Indentation must not use Tab characters
""")


def test_test_ok(style_checker):
    """Style check test against test-ok.java
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('gnatbench', 'test-ok.java')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
