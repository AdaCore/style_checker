"""A simplified clone of e3.os.process.Run

This is to avoid introducing a dependency on e3, in order to allow
users to run these scripts without having to install e3.
"""
import os
from subprocess import Popen, PIPE, STDOUT


def quote_arg(arg):
    """Return the quoted version of the given argument.

    Returns a human-friendly representation of the given argument, but with all
    extra quoting done if necessary.  The intent is to produce an argument
    image that can be copy/pasted on a POSIX shell command (at a shell prompt).
    :param arg: argument to quote
    :type arg: str
    """
    # The empty argument is a bit of a special case, as it does not
    # contain any character that might need quoting, and yet still
    # needs to be quoted.
    if arg == '':
        return "''"

    need_quoting = ('|', '&', ';', '<', '>', '(', ')', '$',
                    '`', '\\', '"', "'", ' ', '\t', '\n',
                    # The POSIX spec says that the following
                    # characters might need some extra quoting
                    # depending on the circumstances.  We just
                    # always quote them, to be safe (and to avoid
                    # things like file globbing which are sometimes
                    # performed by the shell). We do leave '%' and
                    # '=' alone, as I don't see how they could
                    # cause problems.
                    '*', '?', '[', '#', '~')
    for char in need_quoting:
        if char in arg:
            # The way we do this is by simply enclosing the argument
            # inside single quotes.  However, we have to be careful
            # of single-quotes inside the argument, as they need
            # to be escaped (which we cannot do while still inside.
            # a single-quote string).
            arg = arg.replace("'", r"'\''")
            # Also, it seems to be nicer to print new-line characters
            # as '\n' rather than as a new-line...
            arg = arg.replace('\n', r"'\n'")
            return "'%s'" % arg
    # No quoting needed.  Return the argument as is.
    return arg


def command_line_image(cmd):
    """Return a string image of the given command.

    :param cmds: Same as the cmds parameter in the Run.__init__ method.
    :type: list[str]

    :rtype: str

    This method also handles quoting as defined for POSIX shells.
    This means that arguments containing special characters
    (such as a simple space, or a backslash, for instance),
    are properly quoted.  This makes it possible to execute
    the same command by copy/pasting the image in a shell
    prompt.

    The result is expected to be a string that can be sent verbatim
    to a shell for execution.
    """
    return ' '.join((quote_arg(arg) for arg in cmd))


class Run(object):
    """Class to handle processes.

    :ivar cmd: The ``cmds`` argument passed to the __init__ method
        (a command line passed in a list, or a list of command lines passed as
        a list of list).
    :ivar status: The exit status. As the exit status is only meaningful after
        the process has exited, its initial value is None.  When a problem
        running the command is detected and a process does not get
        created, its value gets set to the special value 127.
    :ivar out: process standard output and error.
    """
    def __init__(self, cmd, env=None, ignore_environ=True):
        """Spawn a process.

        :param cmd: A command line: a tool name and its arguments, passed
            in a list. e.g. ['ls', '-a', '.']
        :type cmds: list[str]
        :param env: None, or a dictionary for environment variables
            (e.g. os.environ). If provided, the dictionary completely
            overrides the environment.
        :type env: dict
        :param ignore_environ: Applies only when env parameter is not None.
            When set to True (the default), the only environment variables
            passed to the program are the ones provided by the env parameter.
            Otherwise, the environment passed to the program consists of the
            environment variables currently defined (os.environ) augmented by
            the ones provided in env.
        :type ignore_environ: bool

        :raise OSError: when trying to execute a non-existent file.
        """
        self.cmd = cmd
        self.status = None
        self.out = ''

        if env is not None and not ignore_environ:
            # ignore_environ is False, so get a copy of the current
            # environment and update it with the env dictionnary.
            tmp = os.environ.copy()
            tmp.update(env)
            env = tmp

        p = Popen(cmd, stdout=PIPE, stderr=STDOUT, env=env)
        self.pid = p.pid
        self.out, _ = p.communicate()
        self.status = p.returncode

    def command_line_image(self):
        """Get shell command line image of the spawned command.

        :rtype: str

        This just a convenient wrapper around the function of the same
        name.
        """
        return command_line_image(self.cmd)
