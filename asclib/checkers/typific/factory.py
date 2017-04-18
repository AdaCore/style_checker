import os

from gnatpython.ex import Run

from asclib.checkers import FileCheckerError


def get_file_checker(filename, config):
    _, ext = os.path.splitext(filename)

    if ext in ('.ads', '.adb', '.ada'):
        from asclib.checkers.typific.ada import AdaFileChecker
        return AdaFileChecker(filename, config)

    if ext in ('.c', '.h'):
        from asclib.checkers.typific.c import CFileChecker
        return CFileChecker(filename, config)

    if ext == '.java':
        # Not supported yet!
        return None

    if ext == '.texi':
        from asclib.checkers.typific.texi import TexiFileChecker
        return TexiFileChecker(filename, config)

    if ext in ('.doc', '.ppt', '.xls', '.ps', '.pdf', '.jpg', '.jpeg',
               '.gif', '.bmp'):
        # Binary file, for which no checking is done.
        return None

    if ext == '.py':
        from asclib.checkers.typific.python import PythonFileChecker
        return PythonFileChecker(filename, config)

    if ext == '.js':
        # Not supported yet!
        return None

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
    """
    try:
        p = Run(['file', filename])
        if p.status != 0:
            raise FileCheckerError(
                '%s returned nonzero (%d):' % (p.command_line_image,
                                               p.status),
                p.out)
    except OSError as e:
        return "Failed to run `file %s': %s" % (filename, e)

    return p.out
