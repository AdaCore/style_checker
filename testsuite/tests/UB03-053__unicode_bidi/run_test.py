def test_acceleo(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "acceleo.mtl")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
acceleo.mtl:3: forbidden unicode character at index 16 (U+202D)
""")


def test_ada(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "pck.ads")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
pck.ads:7: forbidden unicode character at index 45 (U+202A)
pck.ads:9: forbidden unicode characters at indices 32 (U+202B), 49 (U+202C)
""")

    # Repeat the same test with "gnat" as the repository name, as we know
    # Ada files in "gnat" can be handled differently compared to the other
    # repositories.
    p = style_checker.run_style_checker("gnat", "pck.ads")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
pck.ads:7: forbidden unicode character at index 45 (U+202A)
pck.ads:9: forbidden unicode characters at indices 32 (U+202B), 49 (U+202C)
""")


def test_bash(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "bash.sh")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
bash.sh:3: forbidden unicode character at index 19 (U+202E)
""")


def test_c(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "c.c")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
c.c:4: forbidden unicode character at index 19 (U+2066)
""")


def test_csh(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "csh.script")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
csh.script:6: forbidden unicode character at index 4 (U+2067)
""")


def test_java(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "java.java")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
java.java:5: forbidden unicode character at index 12 (U+2068)
""")


def test_m(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "m.m")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
m.m:1: forbidden unicode character at index 22 (U+2069)
""")


def test_perl(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "perl.pl")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
perl.pl:3: forbidden unicode character at index 30 (U+202A)
""")


def test_python(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "python.py")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
python.py:3: forbidden unicode character at index 1 (U+202B)
""")


def test_sh(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "sh.script")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
sh.script:3: forbidden unicode character at index 37 (U+202B)
""")


def test_yaml(style_checker):
    style_checker.set_year(2006)
    p = style_checker.run_style_checker("repo", "yaml.yaml")
    style_checker.assertNotEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, """\
yaml.yaml:1: forbidden unicode character at index 21 (U+202C)
""")
