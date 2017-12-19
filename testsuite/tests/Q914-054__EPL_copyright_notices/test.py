from support import *

class TestRun(TestCase):
    def test_epl_single_year_mtl(self):
        """Style check test against epl_single_year.mtl
        """
        self.set_year(2017)
        p = self.run_style_checker('--config=epl.yaml',
                                   'qgen', 'epl_single_year.mtl')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

        # Try the same test, but without the config file.
        # It should fail, because we no longer include the additional
        # config which allows EPL copyright notices.
        p = self.run_style_checker('qgen', 'epl_single_year.mtl')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
epl_single_year.mtl:2: Copyright notice is not correctly formatted
It must look like...

    Copyright (C) 1992-2017, <copyright holder>

... where <copyright holder> can be any of:
    - `AdaCore'
    - `Altran Praxis'
    - `Altran UK Limited'
    - `Free Software Foundation, Inc.'
    - `AdaCore, Altran Praxis'
    - `AdaCore and Altran UK Limited'
    - `AdaCore, Altran UK Limited'
    - `AdaCore and Altran UK'
    - `AdaCore, Altran UK'
""")

    def test_epl_range_mtl(self):
        """Style check test against epl_range.mtl
        """
        self.set_year(2017)
        p = self.run_style_checker('--config=epl.yaml',
                                   'qgen', 'epl_range.mtl')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

        # Try the same test, but without the config file.
        # It should fail, because we no longer include the additional
        # config which allows EPL copyright notices.
        p = self.run_style_checker('qgen', 'epl_range.mtl')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
epl_range.mtl:2: Copyright notice is not correctly formatted
It must look like...

    Copyright (C) 1992-2017, <copyright holder>

... where <copyright holder> can be any of:
    - `AdaCore'
    - `Altran Praxis'
    - `Altran UK Limited'
    - `Free Software Foundation, Inc.'
    - `AdaCore, Altran Praxis'
    - `AdaCore and Altran UK Limited'
    - `AdaCore, Altran UK Limited'
    - `AdaCore and Altran UK'
    - `AdaCore, Altran UK'
""")

    def test_relpath_m(self):
        """Style check test against relpath.m
        """
        self.set_year(2017)
        p = self.run_style_checker('--config=epl.yaml', 'qgen', 'relpath.m')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

        # Try the same test, but without the config file.
        # Since the file has a traditional copyright notice,
        # the test is expected to pass also.
        p = self.run_style_checker('qgen', 'relpath.m')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_deep_notice(self):
        """Style check test against deep_notice.m
        """
        self.set_year(2017)
        p = self.run_style_checker('--config=epl.yaml',
                                   'qgen', 'deep_notice.m')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

        # Try the same test, but without the config file.
        # It should fail, because we no longer include the additional
        # config which allows notices to be deeper than the default.
        p = self.run_style_checker('qgen', 'deep_notice.m')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
deep_notice.m:100: Copyright notice must occur before line 24
""")

    def test_notice_too_deep_m(self):
        """Style check test against notice_too_deep.m
        """
        self.set_year(2017)
        p = self.run_style_checker('--config=epl.yaml',
                                   'qgen', 'notice_too_deep.m')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
notice_too_deep.m:101: Copyright notice must occur before line 100
""")

        # Try the same test, but without the config file.
        # It should fail, because we no longer include the additional
        # config which allows notices to be deeper than the default.
        p = self.run_style_checker('qgen', 'notice_too_deep.m')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
notice_too_deep.m:101: Copyright notice must occur before line 24
""")


if __name__ == '__main__':
    runtests()
