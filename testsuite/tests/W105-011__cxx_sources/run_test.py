import pytest
import shutil


@pytest.mark.parametrize(
    "extension", ("C", "cc", "cpp", "CPP", "c++", "cp", "cxx", "hh", "hpp", "H", "tcc")
)
def test_cxx_source_files(style_checker, extension):
    """Check that C++ source files are recognized as such...

    The way we verify this is by calling the style_checker with
    the "-v" option, which prints a log of the type of file it
    recognizes (or nothing if it doesn't recognize it).
    """
    if extension == "CPP":
        # We couldn't include a copy of the file with that extension
        # in this testcase because we already have a file with the same
        # extension but in lowercase. If we included both files, we would
        # end up with two files in the same repository differing only by
        # their casing, which is not allowed (this causes problems when
        # cloning the repository on OSes where the filesystem casing
        # is case-insensitive). Just create the file on the fly instead,
        # by copying the one with the lowercase casing.
        shutil.copy(f"f.{extension.lower()}", f"f.{extension}")

    style_checker.set_year(2022)
    p = style_checker.run_style_checker("-v", "whatever", f"f.{extension}")
    style_checker.assertEqual(p.status, 0, p.image)
    style_checker.assertRunOutputEqual(p, f"""\
Checking style of `f.{extension}' (C/C++)
""")
