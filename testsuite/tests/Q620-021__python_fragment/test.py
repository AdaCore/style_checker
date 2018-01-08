from shutil import move
from support import *


class TestRun(TestCase):
    def test_conf_py(self):
        """Run checker against conf.py
        """
        p = self.run_style_checker('gnat', 'conf.py')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
conf.py:58:9: E722 do not use bare except'
""")

    def test_conf_frag_py(self):
        """Run checker against conf.frag.py
        """
        p = self.run_style_checker('dummy', 'conf.frag.py')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_conf_with_frag_keyword_py(self):
        """Run checker against conf-with-frag-keyword.py
        """
        p = self.run_style_checker('dummy', 'conf-with-frag-keyword.py')
        self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_conf_bad_pep8_frag_py(self):
        """Run checker against conf-bad-pep8.frag.py
        """
        p = self.run_style_checker('gnat', 'conf-bad-pep8.frag.py')
        self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
conf-bad-pep8.frag.py:10:16: E211 whitespace before '('
conf-bad-pep8.frag.py:58:9: E722 do not use bare except'
""")


if __name__ == '__main__':
    runtests()
