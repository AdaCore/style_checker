def test_comment_ko_1_adb(style_checker):
    """First line is not a comment
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'comment-ko-1.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
comment-ko-1.adb:1: First line must be comment markers only.
""")
