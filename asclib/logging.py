"""Simplistic level-based logging."""
import sys

# By default, no logging (mostly used for debugging).
logging_level = 0


def log_info(message, level=1):
    """Print the info message if logs are enabled at the given level.

    Does nothing if the given level is higher than the current logging
    level.

    :param message: The message to print.
    :type message: str
    :param level: The imortance level of the message. The smaller
        the number, the more important the message.
    :type level: int
    """
    if logging_level < level:
        return
    print(message)


def log_error(error_message):
    """Print the given error message on standard error.

    :param error_message: The error message. When given a list of strings,
        all the strings are joined together with a newline in between.
        A newline is also added at the end of the error message if not
        already terminated by a newline.
    :type error_message: str | list[str]
    """
    if not isinstance(error_message, str):
        # It's a list of strings. Convert to a string with new line
        # characters in between.
        error_message = "\n".join(error_message)
    if not error_message.endswith("\n"):
        error_message += "\n"
    sys.stderr.write(error_message)
