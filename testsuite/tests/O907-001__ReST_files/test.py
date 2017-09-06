from support import *


class TestRun(TestCase):
    def test_bad_directives(self):
        """Style check test against bad_directives.rst
        """
        p = self.run_style_checker('whatever', 'bad_directives.rst')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
bad_directives.rst:7: invalid directive syntax (':' should be '::')
                      .. typo-directive-no-arg:
                                              ^
bad_directives.rst:14: invalid directive syntax (':' should be '::')
                       .. typo-directive-with-args: helo smtp
                                                  ^
bad_directives.rst:23: invalid directive syntax (':' should be '::')
                       .. typo:With-Colors-not:ok:
                                                 ^
bad_directives.rst:25: invalid directive syntax (':' should be '::')
                       .. typo:with-colors-NOT:ok: args1 two
                                                 ^
""")

    def test_gnat_ccg(self):
        """Style check test against gnat_ccg.rst
        """
        p = self.run_style_checker('gnat', 'gnat_ccg.rst')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_the_gnat_configurable_run_time_facility(self):
        """Style check test against the_gnat_configurable_run_time_facility.rst
        """
        p = self.run_style_checker(
            'gnat', 'the_gnat_configurable_run_time_facility.rst')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
