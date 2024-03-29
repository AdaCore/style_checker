def test_missing_EOL_at_EOF(style_checker):
    """Check kmissing EOL at EOF
    """
    style_checker.set_year(2006)
    p = style_checker.run_style_checker('trunk/gnat', 'asistant-funcenum.ads')
    style_checker.assertNotEqual(p.status, 0, p.image)
    # Note that this version of the style_check flags the copyright
    # line as being invalid, because of the lowercase '(c)' instead
    # of the '(C)', but it seems that the same test in the infosys
    # testsuite does not??? Thomas emailed about it on 2017-03-25
    # under NA17-007.
    style_checker.assertRunOutputEqual(p, """\
asistant-funcenum.ads:765: no newline at end of file
asistant-funcenum.ads:9: Copyright notice is not correctly formatted
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
    - `Capgemini Engineering'
    - `AdaCore, Capgemini Engineering'
""")
