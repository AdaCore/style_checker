from shutil import copy
from support import *

class TestRun(TestCase):
    def test_README_dot_BUILD(self):
        """Run checker against README.BUILD
        """
        p = self.run_style_checker('gnat', 'README.BUILD')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
README.BUILD:2: this line is too long (95 > 79 characters)
README.BUILD:3: DOS line ending is not allowed
README.BUILD:3: inconsistent newline: cr+lf [dos] (the previous line used lf [unix])
README.BUILD:4: Trailing spaces are not allowed
README.BUILD:5: no newline at end of file
""")

    def test_README_underscore_BUILD(self):
        """Run checker against README_BUILD
        """
        # Copy README.BUILD as README_BUILD.  Unlike README.BUILD,
        # README_BUILD should not be subjected to any style check,
        # and therefore should not trigger any violation.
        copy('README.BUILD', 'README_BUILD')
        p = self.run_style_checker('gnat', 'README_BUILD')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
