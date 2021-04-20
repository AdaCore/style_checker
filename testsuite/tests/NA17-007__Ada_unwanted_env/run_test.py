import os


def test_banned_env_vars(style_checker):
    """Verify that the style checker ignores some banned env vars
    """
    # Define all the environment variables that our Ada checker
    # should be disabling...
    BANNED_VAR_NAMES = ('GCC_EXEC_PREFIX', 'GCC_INSTALL_DIRECTORY',
                        'GCC_INCLUDE_DIR',
                        'GCC_ROOT', 'GNAT_ROOT', 'BINUTILS_ROOT')
    for var_name in BANNED_VAR_NAMES:
        os.environ[var_name] = '/bad'

    # To do our verification, we create on our fake GCC program
    # which will issue an error message if any of the environment
    # variables that should be unset was in fact unset.
    #
    # This fake GCC is rigged to generate output no matter what,
    # so we can double-check that it is actually being called,
    # and that it does not detect anything wrong (or else it would
    # generate some unexpected output).

    os.environ['PATH'] = "%s:%s" % (
        os.path.join(os.getcwd(), 'bin'),
        os.environ['PATH'])

    style_checker.set_year(2006)
    p = style_checker.run_style_checker('toto', 'ada05-ok-1.adb')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
--- Checking all banned environment variables...
--- Done!
""")
