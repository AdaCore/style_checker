from support import *

class TestRun(TestCase):
    def test_dump_checks(self):
        """Run checker with --dump-checks
        """
        p = self.run_style_checker('--dump-checks')
	self.assertNotEqual(p.status, 0, p.image)
        self.assertRunOutputEqual(p, """\
           STYLE  FEATUR START_ START_ COPYRI COPYRI COPYRI COPYRI ADA_RM  EOL   NO_DOS NO_LAS LENGTH TRAILI  REV
STD_ADA                    X             X      X      X      X      -      X      X      X      -      X      X
RT_SPEC                    X             X      X      X      X      X      X      X      X      -      X      X
RT_BODY                    X             X      X      X      X      -      X      X      X      -      X      X
COMPILER_C                 X             X      X      X      X      -      X      X      X      -      X      X
C                          -             X      X      X      X      -      X      X      X      -      X      X
JAVA                       X             X      X      X      X      -      X      X      X      -      X      X
TEXI                       -             X      X      X      X      -      X      X      X      -      X      -
SH                         -             -      -      -      -      -      X      X      X      -      X      -
BASH                       -             -      -      -      -      -      X      X      X      -      X      -
CSH                        -             -      -      -      -      -      X      X      X      -      X      -
PYTHON                     -             -      -      -      -      -      X      X      -      -      X      -
PERL                       -             -      -      -      -      -      X      X      X      -      X      -
JAVASCRIPT                 -             -      -      -      -      -      X      X      -      -      X      -
""")


if __name__ == '__main__':
    runtests()
