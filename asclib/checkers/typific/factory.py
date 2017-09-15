"""The typific file checker factory...
"""
import os

from asclib.checkers import FileCheckerError
from asclib.ex import Run


def get_file_checker(filename, config):
    """Return the TypificChecker for the given filename.

    :param filename: The name of the file to be checking.
    :type filename: str
    :param config: a Config object.
    :type config: Config
    """
    _, ext = os.path.splitext(filename)

    if ext in ('.ads', '.adb', '.ada'):
        from asclib.checkers.typific.ada import AdaFileChecker
        return AdaFileChecker(filename, config)

    if ext in ('.c', '.h'):
        from asclib.checkers.typific.c import CFileChecker
        return CFileChecker(filename, config)

    if ext == '.java':
        from asclib.checkers.typific.java import JavaFileChecker
        return JavaFileChecker(filename, config)

    if ext == '.texi':
        from asclib.checkers.typific.texi import TexiFileChecker
        return TexiFileChecker(filename, config)

    if ext in ('.doc', '.ppt', '.xls', '.ps', '.pdf', '.jpg', '.jpeg',
               '.gif', '.bmp'):
        # Binary file, for which no checking is done.
        return None

    if ext in ('.py', '.anod', '.plan'):
        from asclib.checkers.typific.python import PythonFileChecker
        return PythonFileChecker(filename, config)

    if ext == '.js':
        from asclib.checkers.typific.javascript import JavascriptFileChecker
        return JavascriptFileChecker(filename, config)

    if ext == '.yaml':
        from asclib.checkers.typific.yaml_files import YamlFileChecker
        return YamlFileChecker(filename, config)

    if ext == '.rst':
        from asclib.checkers.typific.rst import RstFileChecker
        return RstFileChecker(filename, config)

    if filename.startswith('known-problems-'):
        # Known problems files. These are now handled by impactdb.
        # So no need for us to provide a style-checker anymore.
        return None

    if filename.startswith('README.') or \
            filename.startswith('COPYING'):
        from asclib.checkers.typific.gnat_info import GNATInfoFileChecker
        return GNATInfoFileChecker(filename, config)

    # Run "file" to see if what kind of file this might be.
    file_type = get_file_type(filename)

    if 'Bourne shell' in file_type or \
            'POSIX shell' in file_type:
        from asclib.checkers.typific.sh import ShFileChecker
        return ShFileChecker(filename, config)

    if 'Bourne-Again shell' in file_type:
        from asclib.checkers.typific.bash import BashFileChecker
        return BashFileChecker(filename, config)

    if 'C shell' in file_type:
        from asclib.checkers.typific.csh import CshFileChecker
        return CshFileChecker(filename, config)

    if 'Perl script' in file_type:
        from asclib.checkers.typific.perl import PerlFileChecker
        return PerlFileChecker(filename, config)

    if 'python script' in file_type:
        from asclib.checkers.typific.python import PythonFileChecker
        return PythonFileChecker(filename, config)

    # Not a known kind of file...
    return None


def get_file_type(filename):
    """Run `file' on filename and return its output.

    :param filename: The name of the file on which to run the `file'
        command.
    :type filename: str
    """
    try:
        p = Run(['file', filename])
        if p.status != 0:
            raise FileCheckerError(
                '%s returned nonzero (%d):' % (p.command_line_image(),
                                               p.status),
                p.out)
    except OSError as e:
        raise FileCheckerError("Failed to run `file %s': %s" % (filename, e))

    return p.out


def dump_check_for_all_file_types():
    """Implement the --dump-checks command-line switch.

    :rtype: None
    """
    from asclib import get_config_default_filename
    from asclib.config import Config
    config = Config(get_config_default_filename(), 'nothing', 2006)
    gnat_config = Config(get_config_default_filename(), 'gnat', 2006)

    from asclib.checkers.typific.ada import AdaFileChecker
    AdaFileChecker('a.ads', config).dump_checks('STD_ADA', print_header=True)
    AdaFileChecker('a-a.ads', gnat_config).dump_checks('RT_SPEC')
    AdaFileChecker('a-a.adb', gnat_config).dump_checks('RT_BODY')
    AdaFileChecker('bla.adb', gnat_config).dump_checks('COMPILER_CORE')

    from asclib.checkers.typific.c import CFileChecker
    CFileChecker('c.h', config).dump_checks('C')

    from asclib.checkers.typific.java import JavaFileChecker
    JavaFileChecker('j.java', config).dump_checks('JAVA')

    from asclib.checkers.typific.texi import TexiFileChecker
    TexiFileChecker('h.texi', config).dump_checks('TEXI')

    from asclib.checkers.typific.sh import ShFileChecker
    ShFileChecker('s', config).dump_checks('SH')

    from asclib.checkers.typific.bash import BashFileChecker
    BashFileChecker('b', config).dump_checks('BASH')

    from asclib.checkers.typific.csh import CshFileChecker
    CshFileChecker('c', config).dump_checks('CSH')

    from asclib.checkers.typific.python import PythonFileChecker
    PythonFileChecker('p.py', config).dump_checks('PYTHON')

    from asclib.checkers.typific.perl import PerlFileChecker
    PerlFileChecker('p.pl', config).dump_checks('PERL')

    from asclib.checkers.typific.javascript import JavascriptFileChecker
    JavascriptFileChecker('j.js', config).dump_checks('JAVASCRIPT')

    from asclib.checkers.typific.rst import RstFileChecker
    RstFileChecker('a.rst', config).dump_checks('REST', print_footer=True)
