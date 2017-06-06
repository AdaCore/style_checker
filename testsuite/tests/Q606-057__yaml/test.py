from shutil import move
from support import *


class TestRun(TestCase):
    def test_config_yaml(self):
        """Run checker against config.yaml
        """
        p = self.run_style_checker('electrolyt', 'config.yaml')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_config_ko_yaml(self):
        """Run checker against config_ko.yaml
        """
        p = self.run_style_checker('electrolyt', 'config_ko.yaml')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
Error: config_ko.yaml: while parsing a flow sequence
  in "config_ko.yaml", line 10, column 13
expected ',' or ']', but got '<scalar>'
  in "config_ko.yaml", line 12, column 5
""")


if __name__ == '__main__':
    runtests()
