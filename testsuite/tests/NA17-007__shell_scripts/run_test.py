from shutil import move


def test_dummy_bash_sh(style_checker):
    """Run checker against dummy_bash.sh
    """
    p = style_checker.run_style_checker('gnat', 'dummy_bash.sh')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_dummy_csh_script(style_checker):
    """Run checker against dummy_csh.script
    """
    p = style_checker.run_style_checker('gnat', 'dummy_csh.script')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_dummy_perl(style_checker):
    """Run checker against dummy_perl
    """
    p = style_checker.run_style_checker('gnat', 'dummy_perl')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_dummy_python(style_checker):
    """Run checker against dummy_python
    """
    p = style_checker.run_style_checker('gnat', 'dummy_python')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
dummy_python:3:6: E225 missing whitespace around operator
""")


def test_dummy_sh(style_checker):
    """Run checker against dummy_sh
    """
    p = style_checker.run_style_checker('gnat', 'dummy_sh')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_build_sh_ko(style_checker):
    """Run checker against build-sh-ko
    """
    p = style_checker.run_style_checker('gnat', 'build-sh-ko')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
build-sh-ko: 184: Syntax error: "fi" unexpected
""")


def test_make_bin_5(style_checker):
    """Run checker against make-bin-5
    """
    p = style_checker.run_style_checker('/nile.c/cvs/Dev/scripts/nightly',
                               'make-bin-5')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
make-bin-5: 230: Syntax error: "fi" unexpected
""")


def test_sync_uploads(style_checker):
    """Run checker against sync-uploads
    """
    p = style_checker.run_style_checker('gnat', 'sync-uploads')
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEmpty(p)


def test_bash_ko_sh(style_checker):
    """Run checker against bash-ko.sh
    """
    p = style_checker.run_style_checker('unimportant', 'bash-ko.sh')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
bash-ko.sh: line 3: unexpected EOF while looking for matching `}'
bash-ko.sh: line 4: syntax error: unexpected end of file
""")


def test_csh_ko(style_checker):
    """Run checker against bash-ko.sh
    """
    p = style_checker.run_style_checker('unimportant', 'csh-ko.csh')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
if: Expression Syntax.
""")


def test_bad_perl_pl(style_checker):
    """Run checker against bad_perl.pl
    """
    p = style_checker.run_style_checker('unimportant', 'bad_perl.pl')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
syntax error at bad_perl.pl line 3, near "my;"
bad_perl.pl had compilation errors.
""")
