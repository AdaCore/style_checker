def test_binop_py(style_checker):
    """Run checker against binop.py
    """
    p = style_checker.run_style_checker('whatever-repo', 'binop.py')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
