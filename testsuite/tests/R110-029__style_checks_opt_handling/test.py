from support import *


class TestRun(TestCase):
    def test_ada12_adb(self):
        """Style check test against ada12.adb (standard config)

        The purpose of this test is to establish a baseline, and
        verify that checking ada12.adb using the default style_checker
        configuration yields two errors.

        Once established, this will allow us to show that absence of
        those errors when we use alternative configuration files are
        caused by the configuration file.
        """
        self.set_year(2006)
        p = self.run_style_checker('whatever', 'ada12.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
ada12.adb:1: First line must be comment markers only.
ada12.adb: Copyright notice missing, must occur before line 24
""")

    def test_ada12_adb_new_system_config(self):
        """Style check test against ada12.adb (new system config)

        This new system config waves the requirement for a copyright
        header.  So instead of the two errors we get when using
        the standard config, we should be down to 1 error...
        """
        self.set_year(2006)
        p = self.run_style_checker(
            '--system-config=system-conf.yaml',
            'whatever', 'ada12.adb')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
ada12.adb:1: First line must be comment markers only.
""")

    def test_ada12_adb_new_system_config_and_module_config(self):
        """Style check test against ada12.adb (both system and module conf)
        """
        self.set_year(2006)
        p = self.run_style_checker(
            '--system-config=system-conf.yaml',
            '--config=module-conf.yaml',
            'whatever', 'ada12.adb')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
