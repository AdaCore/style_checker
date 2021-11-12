def test_dump_checks(style_checker):
    """Run checker with --dump-checks
    """
    p = style_checker.run_style_checker('--dump-checks')
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
            BIDI  START_ COPYRI ADA_RM NO_TAB  EOL   NO_DOS NO_LAS LENGTH TRAILI  REV
STD_ADA      X      X      X      -      -      X      X      X      -      X      X
RT_SPEC      X      X      X      X      -      X      X      X      -      X      X
RT_BODY      X      X      X      -      -      X      X      X      -      X      X
COMPILER_C   X      X      X      -      -      X      X      X      -      X      X
C            X      -      X      -      -      X      X      X      -      X      X
JAVA         X      X      X      -      X      X      X      X      -      X      X
TEXI         -      -      X      -      -      X      X      X      -      X      -
SH           X      -      -      -      -      X      X      X      -      X      -
BASH         X      -      -      -      -      X      X      X      -      X      -
CSH          X      -      -      -      -      X      X      X      -      X      -
PYTHON       X      -      -      -      -      X      X      X      -      X      -
PERL         X      -      -      -      -      X      X      X      -      X      -
ACCELEO      X      -      X      -      X      X      X      X      -      X      -
.M FILES     X      -      X      -      X      X      X      X      -      X      -
REST         -      -      -      -      -      X      X      X      -      -      -

Legend:
-------
  BIDI: reject characters that could be used to mask malicious code
  START_COMMENT: check that the first line is a comment
  COPYRIGHT: check that file has a well formed copyright notice
  NO_TAB_IDENT: check that tab characters are not used for indentation
  EOL: check that the end of lines are consistent
  NO_DOS_EOL: check that we do not have DOS end-of-line sequences
  NO_LAST_EOL: check that the last line as a line-ending
  LENGTH: check that lines are not too long (79 characters)
  TRAILING: check that we have no trailing whitespaces
  REV: check that we do not have old RCS keywords
""")
