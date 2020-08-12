def test_line_1(style_checker):
    """style_checker on python file with No_Style_Check comment on line 1.

    The file has PEP8 errors, but those should be ignored thanks
    to the No_Style_Check comment.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/line_1.py')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_line_2(style_checker):
    """style_checker on python file with No_Style_Check comment on line 2.

    The file has PEP8 errors, but those should be ignored thanks
    to the No_Style_Check comment.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/line_2.py')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_line_3(style_checker):
    """style_checker on python file with No_Style_Check comment on line 3.

    The file has a valid No_Style_Check except that it's on the third
    line of the file, so it should be too late and ignored by
    the style_checker, and therefore generate a report of all the PEP8
    errors in that file.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/line_3.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
src/line_3.py:9:19: E211 whitespace before '('
""")


def test_space_after(style_checker):
    """style_checker on python file with invalid No_Style_Check comment.

    The file has a No_Style_Check comment, except that that
    the comment is not starting at the end of the line.
    So style_checker ignores it, and lets pep8 report the errors
    in that file.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/space_after.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
src/space_after.py:1:17: W291 trailing whitespace
src/space_after.py:7:19: E211 whitespace before '('
""")


def test_space_before(style_checker):
    """style_checker on python file with invalid No_Style_Check comment.

    The file has a No_Style_Check comment, except that that
    the comment is not starting at the end of the line.
    So style_checker ignores it, and lets pep8 report the errors
    in that file.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/space_before.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
src/space_before.py:5:19: E211 whitespace before '('
""")


def test_space_inside(style_checker):
    """style_checker on python file with invalid No_Style_Check comment.

    The file has a No_Style_Check comment, except that that
    there is more than one space between the # and the No_Style_Check
    keyword. So style_checker ignores it, and lets pep8 report
    the errors in that file.
    """
    p = style_checker.run_style_checker('/trunk/module', 'src/space_inside.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
src/space_inside.py:3:19: E211 whitespace before '('
""")
