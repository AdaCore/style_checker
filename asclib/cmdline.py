from argparse import Action, ArgumentParser
import datetime
import re
import sys

from asclib import get_config_default_filename
from asclib.checkers.typific.factory import dump_check_for_all_file_types


class DumpChecksAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        dump_check_for_all_file_types()
        sys.exit(1)


def parse_cmdline(argv=None):
    parser = ArgumentParser(description='The AdaCore Style Checker')
    parser.add_argument('module_name',
                        help=('The name of module/repository where'
                              ' the file to be checked lives.'))
    parser.add_argument('filenames', metavar='filename', nargs='+',
                        help=('The names of the files to be checked.'))
    parser.add_argument('-config', '--config', metavar='CONFIG_FILENAME',
                        default=get_config_default_filename(),
                        help='The config file to use (default: %(default)s)')

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
