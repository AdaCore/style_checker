from shutil import move
from support import *

class TestRun(TestCase):
    def test_test_py(self):
        """Run checker against test.py
        """
        move('src/test.py.rename_me', 'src/test.py')
        p = self.run_style_checker('/paris.a/cvs/Dev/gps', 'src/test.py')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
