from support import *

class TestRun(TestCase):
    def test_test1(self):
        """Style check test against test1.java
        """
        p = self.run_style_checker('/paris.a/cvs/Dev/gnatbench',
                                   'test1.java')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
test1.java:1: First line must start with a comment (regexp: (/\*|//).*)
test1.java: Copyright notice missing, must occur before line 24
""")

    def test_test1_star_import(self):
        """Style check test against test1-start-import.java

        This is actually the original version of test1.java, which
        apparently used to pass the external-checker check but no
        longer does, because the configuration we now use explicitly
        request that we flag .* import as errors.
        """
        p = self.run_style_checker('gnatbench',
                                   'test1-start-import.java')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
[warning] /usr/bin/checkstyle: JVM flavor 'sunmin5' not understood
[ERROR] test1-start-import.java:1: Using the '.*' form of import should be avoided - java.io.*. [AvoidStarImport]
Checkstyle ends with 1 errors.
""")

    def test_test2(self):
        """Style check test against test2.java

        Note that we removed the import from the original test (from
        the days the style checker was cvs_check, a part of the infosys
        project), because that import uses the .* form, which is now
        explicitly forbidden.
        """
        self.set_year(2006)
        p = self.run_style_checker('gnatbench', 'test2.java')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_test3(self):
        """Style check test against test3.java

        Note that we removed the import from the original test (from
        the days the style checker was cvs_check, a part of the infosys
        project), because that import uses the .* form, which is now
        explicitly forbidden.
        """
        self.set_year(2006)
        p = self.run_style_checker('gnatbench', 'test3.java')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_GNAT_libc(self):
        """Style check test against GNAT_libc.java

        Note that we removed the import from the original test (from
        the days the style checker was cvs_check, a part of the infosys
        project), because that import uses the .* form, which is now
        explicitly forbidden.
        """
        self.set_year(2006)
        p = self.run_style_checker('gnatbench', 'GNAT_libc.java')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
