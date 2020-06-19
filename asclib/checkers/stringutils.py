"""Provide some string-related features that are common in our context."""

# The end-of-line marker in Unix text files, and DOS text files.
UNIX_EOL = '\n'
DOS_EOL = '\r\n'

# A dict whose key is one of the end-of-line strings above, and
# where the value is a human-readable description of that end-of-line
# marker.
PRINTABLE_EOL_MAP = {
    UNIX_EOL: 'lf [unix]',
    DOS_EOL: 'cr+lf [dos]',
    }


def get_eol(line):
    """Return the end-of-line marker from the given string (or None).

    :param line: A string.
    :type line: str
    :return: The end-of-line marker if one is found at the end of
        the given string, or None otherwise.
    :rtype: str | None
    """
    for eol_kind in (DOS_EOL, UNIX_EOL):
        # Note that the order in which we do the checking is
        # important, as UNIX_EOL is a sub-set of the DOS_EOL
        # sequence...
        if line.endswith(eol_kind):
            return eol_kind
    return None
