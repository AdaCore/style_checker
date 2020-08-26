def test_max_line_length(style_checker):
    """Verify the maximum line length for Python is 88 characters.
    """
    def python_statement_from_len(length):
        """Return a string with a python statement of exactly length chars.

        Note that length must be at least ~ 10 characters.
        """
        pre = 'print("'
        post = '")'
        line = '-' * (length - len(pre) - len(post))
        return pre + line + post

    EXPECTED_MAX_LINE_LENGTH = 88

    def test_style_checker_with_len(length):
        """Check style_checker behavior a Python line of length chars."""
        stmt = python_statement_from_len(length)
        py_file_name = "foo{length}.py".format(length=length)

        with open(py_file_name, 'w') as f:
            f.write(stmt + '\n')

        p = style_checker.run_style_checker('whatever', py_file_name)

        if length <= EXPECTED_MAX_LINE_LENGTH:
            style_checker.assertEqual(p.status, 0, p.image)
            style_checker.assertRunOutputEmpty(p)
        else:
            style_checker.assertNotEqual(p.status, 0, p.image)
            style_checker.assertRunOutputEqual(p, """\
{py_file_name}:1:{col}: E501 line too long ({length} > {EXPECTED_MAX_LINE_LENGTH} characters)
""".format(
    py_file_name=py_file_name,
    col=EXPECTED_MAX_LINE_LENGTH + 1,
    length=length,
    EXPECTED_MAX_LINE_LENGTH=EXPECTED_MAX_LINE_LENGTH,
))

    # Test the behavior on a variety of length, some below 80,
    # some between 80 and EXPECTED_MAX_LINE_LENGTH, and some
    # above EXPECTED_MAX_LINE_LENGTH.
    for length in range(75, EXPECTED_MAX_LINE_LENGTH + 5):
        test_style_checker_with_len (length)
