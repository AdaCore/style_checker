from support import *

class TestRun(TestCase):
    def test_good_python(self):
        """Run the style checker on a python file with no error.
        """
        p = self.run_style_checker('/trunk/module', 'src/good.py')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_good_python_with_verbose(self):
        """Verbose run on a python file with no error.

        This is the same as test_good_python, but running the style_checker
        in verbose mode (mostly for coverage)....
        """
        p = self.run_style_checker('/trunk/module', 'src/good.py', '-v')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
Checking style of `src/good.py' (Python script)
""")

    def test_bad_python(self):
        """Run the style checker on a python file with a style violation.
        """
        p = self.run_style_checker('/trunk/module', 'src/bad.py')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
src/bad.py:4:13: E211 whitespace before '('
""")

    def test_nonexistant_python(self):
        """Run the style checker on a python file with no error.
        """
        p = self.run_style_checker('/trunk/module', 'src/hello.py')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
Error: `src/hello.py' is not a valid filename.
""")


if __name__ == '__main__':
    runtests()
