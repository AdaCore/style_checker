import gnatpython.ex
from gnatpython.fileutils import diff

import os
import sys
from tempfile import mkdtemp
import unittest

TEST_DIR = os.path.dirname(sys.modules['__main__'].__file__)
TEST_DIR = os.path.abspath(TEST_DIR)


class TestCase(unittest.TestCase):
    def setUp(self):
        # Create a directory to be used as tmp by this testcase.
        # We want that directory to be inside the testsuite's
        # global tmp directory, so that anything accidently left
        # behind will be automatically caught and cleaned up by
        # the mainloop.
        #
        # The objective is to force the scripts to use this testcase
        # tmp directory during testing, allowing us to verify once
        # the testcase returns that the git-hooks scripts do not leak
        # any temporary files/directories. We do this by force-setting
        # the various environment variables that gnatpython's Env
        # and the tempfile modules use as the default tmp.
        self.testcase_tmp_dir = \
            mkdtemp('', '', os.environ['ASC_TESTSUITE_TMP'])
        os.environ['TMP'] = self.testcase_tmp_dir
        os.environ['TMPDIR'] = self.testcase_tmp_dir

        # Provide the testcase with an attribute which contains
        # the fullpath to the style_checker program, to make it
        # easy to call it.
        lib_dir = os.path.dirname(os.path.realpath(__file__))
        testsuite_dir = os.path.dirname(lib_dir)
        prefix_dir = os.path.dirname(testsuite_dir)
        self.style_checker_exe = os.path.join(prefix_dir, 'style_checker')
        self.forced_year = None

    def tearDown(self):
        # One last check: Verify that the scripts did not leak any
        # temporary files/directories, by looking at the number of
        # files in the testcase tmp dir (we forced all scripts to
        # use this tmp directory during the setUp phase).
        self.assertFalse(os.listdir(self.testcase_tmp_dir))

    def set_year(self, year):
        self.forced_year = year

    def run_style_checker(self, *args, **run_kwargs):
        """Run style_checker with the given arguments.

        Run this repository's style checker (through the "Run" class
        below), and return the corresponding Run object.

        ARGUMENTS
            args: The arguments passed to the style-checker.
            run_kwargs: The keyword arguments passed to the Run class.

        RETURN VALUE
            A Run object.
        """
        cmd = [self.style_checker_exe]
        if self.forced_year is not None:
            cmd.append('--forced-year=%d' % self.forced_year)
        cmd.extend(list(args))
        return Run(cmd, **run_kwargs)

    def enable_unit_test(self):
        """Setup the environment in a way that allows us to perform unit test.
        """
        lib_dir = os.path.dirname(os.path.realpath(__file__))
        testsuite_dir = os.path.dirname(lib_dir)
        prefix_dir = os.path.dirname(testsuite_dir)
        sys.path.insert(0, prefix_dir)

    def assertOutputEqual(self, expected, actual):
        """same as assertEqual but for strings and with a diff if not equal.

        This a convenience function that allows us to quickly diagnose
        what's wrong when the output does not match...
        """
        self.assertEqual(expected, actual,
                         "Diff:\n\n%s" % diff(expected.splitlines(),
                                              actual.splitlines()))

    def assertRunOutputEqual(self, r, expected_out):
        """assert that r.cmd_out is equal to expected_out...

        ... And if the assertion is not met, then produce a useful
        output.
        """
        self.assertEqual(expected_out, r.cmd_out, r.diff(expected_out))

    def assertRunOutputEmpty(self, r):
        """Same as assertRunOutputEqual with an empty expected output.
        """
        self.assertRunOutputEqual(r, '')


def runtests():
    """Call unittest.main.
    """
    unittest.main()


class Run(gnatpython.ex.Run):
    """A gnatpython.ex.Run subclass providing access to a sanitized output.
    """
    @property
    def cmd_out(self):
        """Same as self.out, except that the output is sanitized.

        RETURN VALUE
            A sanitized version of self.out.
        """
        # For now, just return the output unchanged. We'll see if we need
        # this as implement the full array of tests.
        return self.out

    @property
    def image(self):
        """Return an image of the command and its result and output.

        REMARKS
            This assumes that this command has run to completion.
        """
        return '%% %s -> %s\n%s' % (self.command_line_image(),
                                    self.status,
                                    self.cmd_out)

    def diff(self, expected_out):
        """Return self.out followed by a diff self.cmd_out and expected_out.

        PARAMETERS
            expected_out: A string containing the expected output.
        """
        diff_str = diff(expected_out.splitlines(),
                        self.cmd_out.splitlines())
        return '%s\n\nDiff:\n\n%s' % (self.image, diff_str)
