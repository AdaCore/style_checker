from support import runtests, TestCase


class TestRun(TestCase):
    def test_f2020_adb(self):
        """Style check test against f2020.adb."""
        self.set_year(2006)
        p = self.run_style_checker('repo_name', 'f2020.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
f2020.adb:13:22: target_name is an Ada 202x feature
""")

        # Do the same test as above, but saying that the file is
        # part of the gnat repository. In the gnat repository,
        # f2020.adb would be considered a COMPILER_CORE file, and
        # thus would be checked for Ada 2012 compatibilty.

        p = self.run_style_checker('gnat', 'f2020.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
f2020.adb:13:22: target_name is an Ada 202x feature
""")

    def test_f2020_adb_with_gnat2020_config(self):
        """Style check f2020.adb with gnat2020 config."""
        self.set_year(2006)
        p = self.run_style_checker(
            '--config', 'gnat2020_config.yaml', 'repo_name', 'f2020.adb')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

        # Do the same test as above, but saying that the file is
        # part of the gnat repository. In the gnat repository,
        # f2020.adb would be considered a COMPILER_CORE file, and
        # thus would be checked for Ada 2012 compatibilty, regardless
        # of the configuration file saying we should allow Ada 2020.

        p = self.run_style_checker(
            '--config', 'gnat2020_config.yaml', 'gnat', 'f2020.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
f2020.adb:13:22: target_name is an Ada 202x feature
""")


if __name__ == '__main__':
    runtests()
