from argparse import ArgumentParser
import datetime
import re

from asclib import get_config_default_filename


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
