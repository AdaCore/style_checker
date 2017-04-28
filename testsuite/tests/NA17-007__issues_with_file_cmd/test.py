from support import *

class TestRun(TestCase):
    def test_no_file_exe(self):
        """Check behavior when file is missing
        """
        # The way we do this is by changing the PATH to something
        # that does not exist, thus leaving us with no effective PATH,
        # and then call the style_checker_exe through the current
        # python executable.
        saved_path = os.environ['PATH']
        try:
            os.environ['PATH'] = '/non-existent-dir'
            p = Run([sys.executable, self.style_checker_exe,
                     'nothing', 'hello.sh'])
            self.assertNotEqual(p.status, 0, p.image)
            self.assertRunOutputEqual(p, """\
Failed to run `file hello.sh': [Errno 2] No such file or directory, file not found
""")
        finally:
            os.environ['PATH'] = saved_path

    def test_file_returns_nonzero(self):
        """Check behavior when file returns nonzero
        """
        # Don't know how to make "file" fail, so just put our own fake
        # version ahead in the PATH, before we call the style_checker.
        saved_path = os.environ['PATH']
        try:
            os.environ['PATH'] = '%s:%s' % (
                os.path.join(os.getcwd(), 'bin'),
                os.environ['PATH'])
            p = Run([self.style_checker_exe, 'none', 'hello.sh'])
            self.assertNotEqual(p.status, 0, p.image)
            self.assertRunOutputEqual(p, """\
file hello.sh returned nonzero (1):
Error: hello.sh: Cannot determine file type.
""")
        finally:
            os.environ['PATH'] = saved_path

if __name__ == '__main__':
    runtests()
