from support import *


class TestRun(TestCase):
    def test_no_checker(self):
        """Check behavior when the java style checker is missing.
        """
        # The way we do this is by changing the PATH to something
        # that does not exist, thus leaving us with no effective PATH,
        # and then call the style_checker_exe through the current
        # python executable.
        saved_path = os.environ['PATH']
        try:
            os.environ['PATH'] = '/non-existent-dir'
            p = Run([sys.executable, self.style_checker_exe,
                     'notimportant', 'empty.java'])
            self.assertNotEqual(p.status, 0, p.image)
            self.assertRunOutputEqual(p, """\
Failed to run checkstyle: [Errno 2] No such file or directory, checkstyle not found
""")
        finally:
            os.environ['PATH'] = saved_path


if __name__ == '__main__':
    runtests()
