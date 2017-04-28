from shutil import move
from support import *

class TestRun(TestCase):
    def test_known_problems_7_4(self):
        """Run checker against known-problems-7.4
        """
        p = self.run_style_checker('unimportant', 'known-problems-7.4')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
