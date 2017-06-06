from shutil import move
from support import *


class TestRun(TestCase):
    def test_xzutils_anod(self):
        """Run checker against xzutils.anod
        """
        p = self.run_style_checker('anod', 'xzutils.anod')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_xzutils_ko_pep8_anod(self):
        """Run checker against xzutils-ko-pep8.anod
        """
        p = self.run_style_checker('anod', 'xzutils-ko-pep8.anod')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
xzutils-ko-pep8.anod:3:1: E302 expected 2 blank lines, found 1
""")

    def test_xzutils_ko_pyflakes_anod(self):
        """Run checker against xzutils-ko-pyflakes.anod
        """
        p = self.run_style_checker('anod', 'xzutils-ko-pyflakes.anod')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
xzutils-ko-pyflakes.anod:1: undefined name 'spec'
""")


if __name__ == '__main__':
    runtests()
