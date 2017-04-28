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

if __name__ == '__main__':
    runtests()
