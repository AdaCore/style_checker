from support import runtests, TestCase


class TestRun(TestCase):
    def test_pck_2012_adb(self):
        """Style check test against pck_2012.adb."""
        self.set_year(2006)
        p = self.run_style_checker('repo_name', 'pck_2012.ads')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_pck_2012_adb_with_alt_config_forcing_gnat2012(self):
        """Style check test against pck_2012.adb with gnat12 config option."""
        self.set_year(2006)
        p = self.run_style_checker(
           '--config', 'gnat2012_config.yaml', 'repo_name', 'pck_2012.ads')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)


if __name__ == '__main__':
    runtests()
