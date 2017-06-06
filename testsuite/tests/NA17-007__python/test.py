from shutil import move
from support import *


class TestRun(TestCase):
    def test_test_py(self):
        """Run checker against test.py
        """
        move('src/test.py.rename_me', 'src/test.py')
        p = self.run_style_checker('/paris.a/cvs/Dev/gps', 'src/test.py')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
src/test.py:2: 'from GPS_Support import *' used; unable to detect undefined names
""")

    def test_test_py_ok(self):
        """Run checker against test.py (OK version)
        """
        move('src/test.py.rename_me-ok', 'src/test_ok.py')
        p = self.run_style_checker('gps', 'src/test_ok.py')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
