import os

from asclib.cmdline import parse_cmdline
from asclib.checkers import FileCheckerError
from asclib.checkers.typific.factory import get_file_checker
from asclib.config import Config
import asclib.logging
from asclib.logging import log_error


def style_checker(argv=None):
    args = parse_cmdline(argv)
    asclib.logging.logging_level = args.verbose_level

    config = Config(args.config, args.module_name, args.forced_year)

    has_errors = False
    for filename in args.filenames:
        # Before even trying to launch the style checker, first verify
        # that the file exists, and if it doesn't then report the error,
        # and look at the next file to check...
        if not os.path.isfile(filename):
            has_errors = True
            log_error("Error: `%s' is not a valid filename." % filename)
            continue

        checker = get_file_checker(filename, config)
        if checker is None:
            # No checks for this kind of file.
            continue

        try:
            checker.check_file()
        except FileCheckerError as e:
            has_errors = True
            log_error(e)

    return not has_errors
