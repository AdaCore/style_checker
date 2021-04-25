import e3.os.process
import distutils.dir_util
import os
import pytest
import shutil
import sys
import tempfile

from e3.fs import ls, sync_tree


@pytest.fixture(autouse=True, scope="function")
def env_setup(request):
    # Save our current working environment.
    saved_cwd = os.getcwd()
    saved_environ = os.environ.copy()

    # Create a temporary directory inside which we will be working from.
    tmp_dir = tempfile.mkdtemp("", "style_checker-")

    # Create a directory inside our tmp_dir that we'll use for running
    # our testcase.
    work_dir = os.path.join(tmp_dir, "src")
    os.mkdir(work_dir)
    os.chdir(work_dir)

    # Create a directory inside our tmp_dir that we'll tell the tempfile
    # module to use by default (via the appropriate environment variable).
    # The goal is to verify that style-checker doesn't leak any temporary
    # file or directory it might be creating, by verifying at the end
    # of the test that this temporary directory is empty.
    style_checker_tmp_dir = tempfile.mkdtemp("", "style_checker-")
    style_checker_tmp_dir = os.path.join(tmp_dir, "tmp")
    os.mkdir(style_checker_tmp_dir)
    for var_name in ("TMPDIR", "TEMP", "TMP"):
        os.environ[var_name] = style_checker_tmp_dir

    def env_teardown():
        os.environ.clear()
        os.environ.update(saved_environ)

        style_checker_tmp_dir_contents = os.listdir(style_checker_tmp_dir)
        assert not style_checker_tmp_dir_contents, style_checker_tmp_dir_contents

        os.chdir(saved_cwd)
        shutil.rmtree(tmp_dir)

    request.addfinalizer(env_teardown)


class StyleCheckerFixture:
    """A class providing a convenient interface for style_checker testing.

    ATTRIBUTES
        src_prefix_dir: The style_checker sources root directory.
        src_dir: The testcase's source directory.
        work_dir: The (temporary) directory set up for us to run
            a testcase. All necessary files are copied from src_dir
            to this directory before running the testcase.
        style_checker_exe: The path to the style_checker script.
        forced_year: If not None, force all style_checker tests
            to be performed as if this was the current year (an int).
            See the set_year method for additional information.
    """

    def __init__(self, src_prefix_dir, testcase_src_dir, testcase_work_dir):
        """Initialize self.

        PARAMETERS
            src_prefix_dir: Same as the attribute.
            testcase_src_dir: Same as the src_dir attribute.
            testcase_work_dir: Same as the work_dir attribute.
        """
        self.src_prefix_dir = src_prefix_dir
        self.src_dir = testcase_src_dir
        self.work_dir = testcase_work_dir
        self.style_checker_exe = os.path.join(self.src_prefix_dir, "style_checker")
        self.forced_year = None

        # Set the testcase up, by copying everything from the testcase's
        # source directory, into the current directory.
        distutils.dir_util.copy_tree(self.src_dir, self.work_dir)

    def set_year(self, year):
        """Force the year when running the style_checker.

        This is useful when checking test files which have copyright
        years in them. Without it, we'd have to update all our test
        files each year to add the new year to them.

        PARAMETERS
            year: The year we want to call the style_checker with (an int),
                or None, if we do not want to force the year anymore.
        """
        self.forced_year = year

    def run_style_checker(self, *args, **kwargs):
        """Run style_checker with the given arguments.

        Run this repository's style checker (through the "Run" class
        below), and return the corresponding Run object.

        Note: The reason why we use **kwargs to support named arguments
            is that we'd like those named arguments to have a default
            value, and those cannot be listed after the "*args" argument.
            And we use the "*args" argument in order to make simpler to
            call this method. In The vast majority of the cases, we just
            call the style_checker with a couple of arguments, like so:

                obj.run_style_checker('repo_name', 'filename')

            The alternative is to change the "*args" parameter into
            a parameter taking a list, similar to what e3.os.process.Run
            does. But then, it makes the call to style_checker a little
            more cumbersome:

                obj.run_style_checker(['repo_name', 'filename'])

            We document the list of arguments we support in the "ARGUMENTS"
            section just below, and we also raise an exception when
            an unexpected argument is used. So it seems worth slightly
            obscuring the one location where the method is defined
            in favor of the many locations where this method is called.

        ARGUMENTS
            args: The arguments passed to the style-checker.
            use_sys_executable: If True, then call the style_checker via
                the sys.executable Python interpreter. If False (the default),
                the style_checker script is called directly.

                This can be useful when the PATH has been manipulated
                such that the Python interpreter is no longer in the PATH
                (for instance).
            input: Same as in e3.os.process.Run.__init__.

        RETURN VALUE
            A Run object.
        """
        use_sys_executable = False
        # The named parameters to use when calling subprocess.run
        run_kwargs = {"cwd": self.work_dir, "timeout": 60}

        for arg_name, arg_val in kwargs.items():
            if arg_name in ("input",):
                run_kwargs[arg_name] = arg_val
            elif arg_name == "use_sys_executable" and arg_val:
                use_sys_executable = True
            else:
                raise ValueError(
                    "Invalid argument in call to run_style_checker: {}".format(arg_name)
                )

        cmd = []

        if use_sys_executable:
            cmd.append(sys.executable)
        cmd.append(self.style_checker_exe)

        if self.forced_year is not None:
            cmd.append("--forced-year=%d" % self.forced_year)

        cmd.extend(list(args))

        return Run(cmd, **run_kwargs)

    def enable_unit_test(self):
        """Set the environment up to allow us to perform unit tests."""
        sys.path.insert(0, self.src_prefix_dir)

    def make_minimal_copy_of_python_install(self, target_dir, exclude_modules=None):
        """Create a minimal copy of Python in target_dir.

        The goal of this method is to provide a minimal install that
        testcases can then tweak to their testing needs (e.g. manually
        remove some modules).

        PARAMETERS
            target_dir: The directory where the python install should
                be made. If the directory does not exist, it is
                automatically created.
            exclude_modules: If not None, an interable of module names
                that should be excluded from the install.
        """
        src_root_dir = os.path.dirname(os.path.dirname(sys.executable))
        # Make sure src_root_dir is not a symbolic link. Otherwise,
        # sync_tree fails.
        src_root_dir = os.path.realpath(src_root_dir)

        # Only copy the bare minimum of the Python install corresponding
        # to the current interpreter...
        file_list = []
        # ... all bin/python* files...
        file_list.extend(
            os.path.relpath(p, src_root_dir)
            for p in ls(os.path.join(src_root_dir, "bin", "python*"))
        )
        # ... all lib/*python* files and directories (e.g.
        # lib/libpythonX.Y.a or the lib/pythonX.Y/ directory).
        file_list.extend(
            os.path.relpath(p, src_root_dir)
            for p in ls(os.path.join(src_root_dir, "lib", "*python*"))
        )

        if exclude_modules is None:
            ignore = None
        else:
            ignore = []
            site_pkg_dir = os.path.join(src_root_dir, "lib", "python*", "site-packages")
            for module_name in exclude_modules:
                ignore.extend(
                    os.path.relpath(p, src_root_dir)
                    for p in ls(os.path.join(site_pkg_dir, f"{module_name}*"))
                )

        sync_tree(
            source=src_root_dir, target=target_dir, ignore=ignore, file_list=file_list,
        )

    def assertEqual(self, lhs, rhs, msg_if_fails):
        """Verify that lhs is equal to rhs or else raise a failed assertion.

        PARAMETERS
            lhs: The first value to check for equality.
            rhs: The other value to check for equality.
            msg_if_fails: A message to print if the assertion fails.
        """
        assert lhs == rhs, msg_if_fails

    def assertNotEqual(self, lhs, rhs, msg_if_fails):
        """Verify that lhs is not equal to rhs or raise a failed assertion.

        PARAMETERS
            lhs: The first value to check for inequality.
            rhs: The other value to check for inequality.
            msg_if_fails: A message to print if the assertion fails.
        """
        assert lhs != rhs, msg_if_fails

    def assertOutputEqual(self, expected, actual):
        """Verify that the two given strings are equal.

        This method is only provided for legacy reasons, and new testcases
        are encouraged to use the equality operator directly:

        In its previous life (where the testsuite was implemented
        using a framework based on unittest.TestCase), this method
        provided a diff when the output and expected output did not match.

        With the current testsuite framework, the diff is already
        provided by the testsuite framework, so this method
        is no longer very useful. It was kept to help accelerate
        the conversion of the testcases from the old testsuite
        framework, to the new one.

        PARAMETER
            expected: The expected value for our string.
            actual: The actual value.
        """
        assert actual == expected

    def assertRunOutputEqual(self, r, expected_out):
        """Verify that the output from the given Run object is as expected.

        In its previous life (where the testsuite was implemented
        using gnatpython's framework), this method provided a diff
        when the output and expected output did not match.

        With the current testsuite framework, the diff is already
        provided by the testsuite framework, so this method
        is no longer very useful. It was kept to help accelerate
        the conversion of the testcases from the old testsuite
        framework, to the new one.

        PARAMETERS
            r: A Run object.
            expected_out: The expected output.
        """
        assert r.cmd_out == expected_out

    def assertRunOutputEmpty(self, r):
        """Verify that the output from the given Run object is empty.

        In its previous life (where the testsuite was implemented
        using gnatpython's framework), this method provided a diff
        when the output and expected output did not match.

        With the current testsuite framework, the diff is already
        provided by the testsuite framework, so this method
        is no longer very useful. It was kept to help accelerate
        the conversion of the testcases from the old testsuite
        framework, to the new one.

        PARAMETERS
            r: A Run object.
        """
        self.assertRunOutputEqual(r, "")


@pytest.fixture(scope="function")
def style_checker(pytestconfig, request):
    """Return a StyleCheckerFixture."""
    testcase_script_filename = request.fspath.strpath
    testcase_src_dir = os.path.dirname(testcase_script_filename)
    return StyleCheckerFixture(
        src_prefix_dir=pytestconfig.rootdir.strpath,
        testcase_src_dir=testcase_src_dir,
        testcase_work_dir=os.getcwd(),
    )


class Run(e3.os.process.Run):
    """An e3.os.process.Run subclass with a few extra bells and whistles..."""

    @property
    def cmd_out(self):
        """Same as self.out, except that the output is sanitized.

        :return: A sanitized version of self.out.
        """
        # For now, just return the output unchanged. We'll see if we need
        # this as implement the full array of tests.
        return self.out

    @property
    def image(self):
        """Return the command's followed by its statuscode and output.

        REMARKS
            This assumes that this command has run to completion.
        """
        return "%% %s -> %s\n%s" % (
            self.command_line_image(),
            self.status,
            self.cmd_out,
        )
