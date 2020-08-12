def test_markdown_with_python_code(style_checker):
    """Check length-ko-1.adb
    """
    # Run the style_checker with -v to make sure that absolutely
    # no checker of any kind gets triggered.
    p = style_checker.run_style_checker('-v', 'whatever', '2_ENVIRONMENT.md')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)
