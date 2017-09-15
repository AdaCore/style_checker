from support import *

class TestRun(TestCase):
    def test_no_pep8(self):
        """Check behavior when pep8 is missing
        """
        # This is really tricky, because we want to test a situation
        # where pep8 is missing, except we use gnatpython to run
        # our testsuite and gnatpython actually provides pep8! And
        # we also need python to run our style_checker_exe as well.
        #
        # So, the way we do this is by changing the PATH to something
        # that does not exist, thus leaving us with no effective PATH,
        # and then call the style_checker_exe through the current
        # python executable.
        saved_path = os.environ['PATH']
        try:
            os.environ['PATH'] = '/non-existent-dir'
            p = Run([sys.executable, self.style_checker_exe,
                     '/trunk/module', 'src/simple.py'])
            self.assertNotEqual(p.status, 0, p.image)
            self.assertRunOutputEqual(p, """\
Failed to run pep8: [Errno 2] No such file or directory
""")
        finally:
            os.environ['PATH'] = saved_path

if __name__ == '__main__':
    runtests()
