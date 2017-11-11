from support import *

class TestRun(TestCase):
    def test_hl_t_a_01a_ada(self):
        """Style check test against hl_t_a_01a.ada
        """
        self.set_year(2006)
        p = self.run_style_checker('/paris.a/cvs/Dev/erb', 'hl_t_a_01a.ada')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_hl_t_a_02a_ada(self):
        """Style check test against hl_t_a_02a.ada
        """
        self.set_year(2006)
        p = self.run_style_checker('/paris.a/cvs/Dev/erb', 'hl_t_a_02a.ada')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
hl_t_a_02a.ada:9: Copyright notice is not correctly formatted
It must look like...

    Copyright (C) 1992-2006, <copyright holder>

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
    - `The European Space Agency'
""")


if __name__ == '__main__':
    runtests()
