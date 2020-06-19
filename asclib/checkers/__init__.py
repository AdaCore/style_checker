class FileCheckerError(Exception):
    """The exception raised when detecting an error during style checking.

    The argument can be a string (the description of the error), or
    a list of strings, if the description of the error spans over
    multiple lines.
    """

    pass
