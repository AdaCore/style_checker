import os


def test_hello(style_checker):
    """Style check test against hello.js
    """
    p = style_checker.run_style_checker('gnat', 'hello.js')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_hello_double_quotes(style_checker):
    """Style check test against hello-double-quotes.js
    """
    p = style_checker.run_style_checker('qmachine_ts', 'hello-double-quotes.js')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
----- FILE  :  %s/hello-double-quotes.js -----
Line 1, E:0131: Single-quoted string preferred over double-quoted string.
Found 1 error, including 0 new errors, in 1 file (0 files OK).
\a
Some of the errors reported by GJsLint may be auto-fixable using the script
fixjsstyle. Please double check any changes it makes and report any bugs. The
script can be run by executing:

fixjsstyle hello-double-quotes.js 
""" % os.getcwd())


def test_hello_no_style_check_1(style_checker):
    """Style check test against hello-no-style-check-1.js

    There is a no-style-check comment on the first line that
    should prevent the external checker to be run. Otherwise,
    if we do run the checker, it'll report the errors about
    using double-quotes instead of single-quotes.
    """
    p = style_checker.run_style_checker('gnat', 'hello-no-style-check-1.js')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_hello_no_style_check_2(style_checker):
    """Style check test against hello-no-style-check-2.js

    There is a no-style-check comment on the second line that
    should prevent the external checker to be run. Otherwise,
    if we do run the checker, it'll report the errors about
    using double-quotes instead of single-quotes.
    """
    p = style_checker.run_style_checker('a_modeling', 'hello-no-style-check-2.js')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_hello_no_style_check_3(style_checker):
    """Style check test against hello-no-style-check-3.js

    There is a no-style-check comment on the third line, which
    is now too late for it to be effective. So we should be
    running the external checker, and get the double-quote
    style violations about this file.
    """
    p = style_checker.run_style_checker('gnat', 'hello-no-style-check-3.js')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
----- FILE  :  %s/hello-no-style-check-3.js -----
Line 4, E:0131: Single-quoted string preferred over double-quoted string.
Found 1 error, including 0 new errors, in 1 file (0 files OK).
\a
Some of the errors reported by GJsLint may be auto-fixable using the script
fixjsstyle. Please double check any changes it makes and report any bugs. The
script can be run by executing:

fixjsstyle --nojsdoc hello-no-style-check-3.js 
""" % os.getcwd())
