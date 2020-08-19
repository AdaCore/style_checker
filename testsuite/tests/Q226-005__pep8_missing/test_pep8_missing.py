import os
import sys


def test_no_pep8(style_checker):
    """Check behavior when pep8 is missing
    """
    # This is really tricky, because we want to test a situation
    # where pycodestyle is missing, except the testsuite uses a version
    # of Python which we expect to provide pycodestyle.
    #
    # In the past, we worked around this by setting up the PATH
    # so as to make not a single executable can be found from there,
    # and then called the style_checker somewhat artificially
    # via sys.executable. This trick doesn't work anymore for
    # Python anymore, because the checker for Python files now
    # calls pycodestyle via self.executable.
    #
    # So, instead, what we do create a temporary copy of the Python
    # install in our testsuite directory where the pycodestyle module
    # was manually removed.

    local_python_dir = os.path.join(os.getcwd(), "local-python")
    style_checker.make_minimal_copy_of_python_install(
        target_dir=local_python_dir, exclude_modules=("pycodestyle",),
    )
    local_python_exe = os.path.join(
        local_python_dir, "bin", os.path.basename(sys.executable)
    )

    saved_path = os.environ["PATH"]
    try:
        os.environ["PATH"] = os.path.join(local_python_dir, "bin")
        p = style_checker.run_style_checker("/trunk/module", "src/simple.py")
        style_checker.assertNotEqual(p.status, 0, p.image)
        style_checker.assertRunOutputEqual(
            p,
            f"""\
{local_python_exe}: No module named pycodestyle
""",
        )
    finally:
        os.environ["PATH"] = saved_path
