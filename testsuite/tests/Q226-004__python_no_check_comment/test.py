from support import *

class TestRun(TestCase):
    def test_line_1(self):
        """style_checker on python file with No_Style_Check comment on line 1.

        The file has PEP8 errors, but those should be ignored thanks
        to the No_Style_Check comment.
        """
        p = self.run_style_checker('/trunk/module', 'src/line_1.py')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_line_2(self):
        """style_checker on python file with No_Style_Check comment on line 2.

        The file has PEP8 errors, but those should be ignored thanks
        to the No_Style_Check comment.
        """
        p = self.run_style_checker('/trunk/module', 'src/line_2.py')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_line_3(self):
        """style_checker on python file with No_Style_Check comment on line 3.

        The file has a valid No_Style_Check except that it's on the third
        line of the file, so it should be too late and ignored by
        the style_checker, and therefore generate a report of all the PEP8
        errors in that file.
        """
        p = self.run_style_checker('/trunk/module', 'src/line_3.py')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
src/line_3.py:9:19: E211 whitespace before '('
""")

    def test_space_after(self):
        """style_checker on python file with invalid No_Style_Check comment.

        The file has a No_Style_Check comment, except that that
        the comment is not starting at the end of the line.
        So style_checker ignores it, and lets pep8 report the errors
        in that file.
        """
        p = self.run_style_checker('/trunk/module', 'src/space_after.py')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
src/space_after.py:1:17: W291 trailing whitespace
src/space_after.py:7:19: E211 whitespace before '('
""")

    def test_space_before(self):
        """style_checker on python file with invalid No_Style_Check comment.

        The file has a No_Style_Check comment, except that that
        the comment is not starting at the end of the line.
        So style_checker ignores it, and lets pep8 report the errors
        in that file.
        """
        p = self.run_style_checker('/trunk/module', 'src/space_before.py')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
src/space_before.py:5:19: E211 whitespace before '('
""")

    def test_space_inside(self):
        """style_checker on python file with invalid No_Style_Check comment.

        The file has a No_Style_Check comment, except that that
        there is more than one space between the # and the No_Style_Check
        keyword. So style_checker ignores it, and lets pep8 report
        the errors in that file.
        """
        p = self.run_style_checker('/trunk/module', 'src/space_inside.py')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
src/space_inside.py:3:19: E211 whitespace before '('
""")

if __name__ == '__main__':
    runtests()
