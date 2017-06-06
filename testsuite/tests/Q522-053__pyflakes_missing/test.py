from support import *
import os

class TestRun(TestCase):
    def test_no_pyflakes(self):
        """Check behavior when pyflake is missing
        """
        # This is really tricky, because we want to test a situation
        # where pyflakes is missing, except we use gnatpython to run
        # our testsuite and gnatpython actually provides pyflakes!
        # We also need python to run our style_checker_exe as well.
        # And to make things even more difficult, we also need to
        # first get past the pep8 check without error before we get
        # to the point we want to test.
        #
        # So, the way we do this is by: (1) providing our own fake
        # version of pep8 which does nothing; (2) changing the PATH
        # to point to that pep8 and nothing else; And (3), because
        # we no longer have anything on the PATH other than pep8,
        # we call the style_checker_exe through the current python
        # executable.
        saved_path = os.environ['PATH']
        try:
            os.environ['PATH'] = os.path.join(os.getcwd(), 'bin')
            p = Run([sys.executable, self.style_checker_exe,
                     'module', 'src/simple.py'])
            self.assertNotEqual(p.status, 0, p.image)
            self.assertRunOutputEqual(p, """\
Failed to run pyflakes: [Errno 2] No such file or directory, pyflakes not found
""")
        finally:
            os.environ['PATH'] = saved_path

if __name__ == '__main__':
    runtests()
