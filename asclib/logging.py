import sys

logging_level = 0


def log_info(message, level=1):
    if logging_level < level:
        return
    print(message)


def log_error(error_message):
    if not isinstance(error_message, str):
        # It's a list of strings. Convert to a string with new line
        # characters in between.
        error_message = '\n'.join(error_message)
    if not error_message.endswith('\n'):
        error_message += '\n'
    sys.stderr.write(error_message)
