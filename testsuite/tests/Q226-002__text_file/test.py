from support import *

class TestRun(TestCase):
    def test_good_python(self):
        """Run the style checker on a python file with no error.
        """
        p = self.run_style_checker('/trunk/module', 'src/check_me.txt')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
