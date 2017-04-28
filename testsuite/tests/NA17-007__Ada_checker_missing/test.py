from support import *

class TestRun(TestCase):
    def test_no_gnat(self):
        """Check behavior when gnat is missing
        """
        # The way we do this is by changing the PATH to something
        # that does not exist, thus leaving us with no effective PATH,
        # and then call the style_checker_exe through the current
        # python executable.
        saved_path = os.environ['PATH']
        try:
            os.environ['PATH'] = '/non-existent-dir'
            p = Run([sys.executable, self.style_checker_exe,
                     'whatever', 'pck.ads'])
            self.assertNotEqual(p.status, 0, p.image)
            self.assertRunOutputEqual(p, """\
Failed to run gcc: [Errno 2] No such file or directory, gcc not found
""")
        finally:
            os.environ['PATH'] = saved_path

if __name__ == '__main__':
    runtests()
