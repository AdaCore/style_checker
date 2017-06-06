from shutil import move
from support import *


class TestRun(TestCase):
    def test_linux_plan(self):
        """Run checker against linux.plan
        """
        p = self.run_style_checker('electrolyt', 'linux.plan')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_linux_ko_plan(self):
        """Run checker against linux-ko.plan
        """
        p = self.run_style_checker('electrolyt', 'linux-ko.plan')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
linux-ko.plan:11:24: E251 unexpected spaces around keyword / parameter equals
linux-ko.plan:11:26: E251 unexpected spaces around keyword / parameter equals
linux-ko.plan:12:15: E211 whitespace before '('
""")


if __name__ == '__main__':
    runtests()
