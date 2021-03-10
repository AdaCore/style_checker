def test_e203(style_checker):
    """Run checker against a couple of Python files...
    """
    p = style_checker.run_style_checker('whatever-repo', 'e203.py')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)

    # Try the same, but with a "Python fragment", this time.
    p = style_checker.run_style_checker('whatever-repo', 'e203.plan')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
