from support import *

class TestRun(TestCase):
    def test_markdown_with_python_code(self):
        """Check length-ko-1.adb
        """
        # Run the style_checker with -v to make sure that absolutely
        # no checker of any kind gets triggered.
        p = self.run_style_checker('-v', 'whatever', '2_ENVIRONMENT.md')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
