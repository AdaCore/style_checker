import os


def test_no_pep8(style_checker):
    """Check behavior when the java style checker is missing.
    """
    # The way we do this is by changing the PATH to something
    # that does not exist, thus leaving us with no effective PATH,
    # and then call the style_checker_exe through the current
    # python executable.
    saved_path = os.environ['PATH']
    try:
        os.environ['PATH'] = '/non-existent-dir'
        p = style_checker.run_style_checker('notimportant', 'empty.js',
                                   use_sys_executable=True)
        style_checker.assertNotEqual(p.status, 0, p.image)
        style_checker.assertRunOutputEqual(p, """\
Failed to run gjslint: [Errno 2] No such file or directory: 'gjslint'
""")
    finally:
        os.environ['PATH'] = saved_path
