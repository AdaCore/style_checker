def test_bad_and_bad(style_checker):
    """Style check test against bad + bad
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('hello',
                               'ada12-no-first-line-comment.adb',
                               'gprep_check-ko.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
""")


def test_stdin_bad_and_bad(style_checker):
    """Style check test against bad + bad (via stdin)
    """
    style_checker.set_year(2006)
    stdin_buf = '\n'.join(['ada12-no-first-line-comment.adb',
                           'gprep_check-ko.adb'])
    p = style_checker.run_style_checker('hello',
                               input='|' + stdin_buf)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
""")


def test_bad_good_bad_max_failures_1(style_checker):
    """Style check test --max-files-with-failures=1 against
    bad + good + bad
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('--max-files-with-errors=1',
                               'hello',
                               'gprep_check-ko.adb',
                               'ada12.adb',
                               'ada12-no-first-line-comment.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
[other files with style violations were found]
""")


def test_stdin_bad_good_bad_max_failures_1(style_checker):
    """Style check test --max-files-with-failures=1 against
    bad + good + bad (stdin)
    """
    style_checker.set_year(2006)
    stdin_buf = '\n'.join(['gprep_check-ko.adb',
                           'ada12.adb',
                           'ada12-no-first-line-comment.adb',
                           'gprep_check-ko.adb'])
    p = style_checker.run_style_checker('--max-files-with-errors=1',
                               'hello',
                               input='|' + stdin_buf)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
[other files with style violations were found]
""")


def test_bad_good_bad(style_checker):
    """Style check test against bad + good + bad
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('hello',
                               'gprep_check-ko.adb',
                               'ada12.adb',
                               'ada12-no-first-line-comment.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
""")


def test_stdin_bad_good_bad(style_checker):
    """Style check test against bad + good + bad (stdin)
    """
    style_checker.set_year(2006)
    stdin_buf = '\n'.join(['gprep_check-ko.adb',
                           'ada12.adb',
                           'ada12-no-first-line-comment.adb'])
    p = style_checker.run_style_checker('hello',
                               input='|' + stdin_buf)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
""")


def test_bad_bad_good_bad(style_checker):
    """Style check test against bad + bad + good + bad
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('hello',
                               'gprep_check-ko.adb',
                               'empty.adb',
                               'ada12.adb',
                               'ada12-no-first-line-comment.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
empty.adb:1:01: warning: file contains no compilation units [enabled by default]
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
""")


def test_stdin_bad_bad_good_bad(style_checker):
    """Style check test against bad + bad + good + bad (stdin)
    """
    style_checker.set_year(2006)
    stdin_buf = '\n'.join(['gprep_check-ko.adb',
                           'empty.adb',
                           'ada12.adb',
                           'ada12-no-first-line-comment.adb'])
    p = style_checker.run_style_checker('hello',
                               input='|' + stdin_buf)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
empty.adb:1:01: warning: file contains no compilation units [enabled by default]
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
""")


def test_bad_bad_good_bad_good_bad(style_checker):
    """Style check test against bad + bad + good + bad + good + bad
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('hello',
                               'gprep_check-ko.adb',
                               'empty.adb',
                               'ada12.adb',
                               'ada12-no-first-line-comment.adb',
                               'test1.java',
                               'bash-ko.sh')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
empty.adb:1:01: warning: file contains no compilation units [enabled by default]
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
[other files with style violations were found]
""")


def test_bad_nonexistant_good_bad_good_bad(style_checker):
    """Style check test against bad + nonexistant + good + bad + good + bad
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('hello',
                               'gprep_check-ko.adb',
                               'does-not-exist.adb',
                               'ada12.adb',
                               'ada12-no-first-line-comment.adb',
                               'test1.java',
                               'bash-ko.sh')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
Error: `does-not-exist.adb' is not a valid filename.
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
[other files with style violations were found]
""")


def test_bad_bad_good_bad_good_noexistant(style_checker):
    """Style check test against bad + bad + good + bad + good + bad
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('hello',
                               'gprep_check-ko.adb',
                               'empty.adb',
                               'ada12.adb',
                               'ada12-no-first-line-comment.adb',
                               'test1.java',
                               'does-not-exist.py')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
empty.adb:1:01: warning: file contains no compilation units [enabled by default]
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
[other files with style violations were found]
""")


def test_stdin_one_good(style_checker):
    """Style check test against good (via stdin)
    """
    style_checker.set_year(2006)
    stdin_buf = '\n'.join(['ada12.adb'])
    p = style_checker.run_style_checker('hello',
                               input='|' + stdin_buf)
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_stdin_one_bad(style_checker):
    """Style check test against bad (via stdin)
    """
    style_checker.set_year(2006)
    stdin_buf = '\n'.join(['ada12-no-first-line-comment.adb'])
    p = style_checker.run_style_checker('hello',
                               input='|' + stdin_buf)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
""")


def test_stdin_bad_empty_and_bad(style_checker):
    """Style check test against bad + emtpy entry + bad (via stdin)

    The empty entry is to test our defensive programing of this case
    (which otherwise is not expected to happen)
    """
    style_checker.set_year(2006)
    stdin_buf = '\n'.join(['ada12-no-first-line-comment.adb',
                           'gprep_check-ko.adb'])
    p = style_checker.run_style_checker('hello',
                               input='|' + stdin_buf)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
""")


def test_stdin_bad_and_bad_with_terminating_newline(style_checker):
    """Style check test against bad + bad (via stdin, where last has \n)

    The empty entry is to test our defensive programing of this case
    (which otherwise is not expected to happen)
    """
    style_checker.set_year(2006)
    stdin_buf = ('\n'.join(['ada12-no-first-line-comment.adb',
                           'gprep_check-ko.adb']) +
                 '\n')
    p = style_checker.run_style_checker('hello',
                               input='|' + stdin_buf)
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
ada12-no-first-line-comment.adb:1: First line must be comment markers only.
gprep_check-ko.adb:9:16: (style) space not allowed
gprep_check-ko.adb:11:21: (style) space not allowed
""")
