from argparse import Action, ArgumentParser
import datetime
import re
import sys

from asclib import get_system_config_default_filename
from asclib.checkers.typific.factory import dump_check_for_all_file_types

MAX_FILES_WITH_STYLE_FAILURES = 3


class DumpChecksAction(Action):
    """The class used to implement the --dump-checks switch.

    We use this class, because the behavior of the switch is
    similar to the --help switch, where the switch causes
    some information to be printed before we exit. We also
    want the switch to work even if some mandatory positional
    arguments or switches are missing.
    """

    def __call__(self, parser, namespace, values, option_string=None):
        dump_check_for_all_file_types()
        sys.exit(1)


def parse_cmdline(argv=None):
    """Parse the given command-line.

    :param argv: Same as argparse.ArgumentParser.parse_args.
    :type argv: list | None
    """
    parser = ArgumentParser(description='The AdaCore Style Checker')
    parser.add_argument('module_name',
                        help=('The name of module/repository where'
                              ' the file to be checked lives.'))
    parser.add_argument('filenames', metavar='filename', nargs='*',
                        help=('The names of the files to be checked.'
                              ' If no filename is provided, then read'
                              ' the list of files to check from standard'
                              ' input (one file per line). Passing'
                              ' the filenames via standard input allows'
                              ' bypassing potential limitations regarding'
                              ' command-line maximum lengths.'))
    parser.add_argument('--system-config', metavar='CONFIG_FILENAME',
                        default=get_system_config_default_filename(),
                        help=('The system config file to use'
                              ' (default: %(default)s)'))
    parser.add_argument('--config', '-c', dest='module_config',
                        metavar='CONFIG_FILENAME',
                        help=('An additional configuration file providing'
                              ' module-specific settings.'))
    parser.add_argument('--max-files-with-errors', metavar='N',
                        dest='max_files_with_errors',
                        type=int, default=MAX_FILES_WITH_STYLE_FAILURES,
                        help=('Indicates the number of files with style'
                              ' violations after which we abort.'))

    debug = parser.add_argument_group('Testing and Debugging')
    debug.add_argument('--verbose', '-v', dest='verbose_level',
                       default=0, action='count',
                       help=('Output verbose information about processing'))
    debug.add_argument('--forced-year', '-D', metavar='YEAR',
                       default=datetime.date.today().year, type=int,
                       help=('Option to pretend today is a different year'
                             ' than it really is (used mostly to simplify'
                             ' testing'))
    debug.add_argument('--dump-checks', nargs=0, action=DumpChecksAction,
                       help=('Dump the list of checks performed for each'
                             ' kind of file.'))

    args = parser.parse_args(argv)

    # Transform the module_name argument to strip all unnecessary info,
    # and only keep the actual module name.  Eventually, we'll be called
    # with just the module name already stripped, but in the meantime,
    # this helps isolate the rest of the code from a CVS/SVN detail.

    m = re.search(r'(/cvs/Dev|^trunk|^branches(/global/[^/]*)?)/([^/]*)',
                  args.module_name)
    if m is not None:
        args.module_name = m.group(3)

    return args
