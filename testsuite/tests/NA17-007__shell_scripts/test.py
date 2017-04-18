from shutil import move
from support import *

# dummy_sh
class TestRun(TestCase):
    def test_dummy_bash_sh(self):
        """Run checker against dummy_bash.sh
        """
        p = self.run_style_checker('gnat', 'dummy_bash.sh')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_dummy_csh_script(self):
        """Run checker against dummy_csh.script
        """
        p = self.run_style_checker('gnat', 'dummy_csh.script')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_dummy_perl(self):
        """Run checker against dummy_perl
        """
        p = self.run_style_checker('gnat', 'dummy_perl')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_dummy_python(self):
        """Run checker against dummy_python
        """
        p = self.run_style_checker('gnat', 'dummy_python')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
dummy_python:3:6: E225 missing whitespace around operator
""")

    def test_dummy_sh(self):
        """Run checker against dummy_sh
        """
        p = self.run_style_checker('gnat', 'dummy_sh')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

    def test_build_sh_ko(self):
        """Run checker against build-sh-ko
        """
        p = self.run_style_checker('gnat', 'build-sh-ko')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
build-sh-ko: 184: build-sh-ko: Syntax error: "fi" unexpected
""")

    def test_make_bin_5(self):
        """Run checker against make-bin-5
        """
        p = self.run_style_checker('/nile.c/cvs/Dev/scripts/nightly',
                                   'make-bin-5')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
make-bin-5: 230: make-bin-5: Syntax error: "fi" unexpected
""")

    def test_sync_uploads(self):
        """Run checker against sync-uploads
        """
        p = self.run_style_checker('gnat', 'sync-uploads')
	self.assertEqual(p.status, 0, p.image)
        self.assertRunOutputEmpty(p)

if __name__ == '__main__':
    runtests()
