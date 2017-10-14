from support import *

class TestRun(TestCase):
    def test_test2(self):
        """Style check test against test2.java
        """
        self.set_year(2006)
        p = self.run_style_checker('gnatbench', 'test2.java')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
test2.java:10: Trailing spaces are not allowed
test2.java:11: Indentation must not use Tab characters
test2.java:12: Indentation must not use Tab characters
test2.java:13: Indentation must not use Tab characters
""")

    def test_test3(self):
        """Style check test against test3.java
        """
        self.set_year(2006)
        p = self.run_style_checker('gnatbench', 'test3.java')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
test3.java:8: Indentation must not use Tab characters
test3.java:9: Indentation must not use Tab characters
""")

    def test_test_ok(self):
        """Style check test against test-ok.java
        """
        self.set_year(2006)
        p = self.run_style_checker('gnatbench', 'test-ok.java')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
