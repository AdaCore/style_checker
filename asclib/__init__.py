import os


def get_prefix_dir():
    """Return the fullpath of the directory where this tool is installed.

    :return: The location where this tool is installed.
    :rtype: str
    """
    this_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(this_dir)
    return root_dir


def get_system_config_default_filename():
    """Return the full path of the default configuration file.

    :return: The fullpath of the defauld configuration file. This is
        the file that gets used unless an alternate config file is
        specified via the command-line.
    :rtype: str
    """
    return os.path.join(get_prefix_dir(), "etc", "asc_config.yaml")


def get_ada_preprocessing_filename():
    """Return the full path of the "gprep" file used by the Ada checker.

    See the Ada type checker for more information about that file.

    :return: The fullpath of the "gprep" file.
    :rtype: str
    """
    return os.path.join(get_prefix_dir(), "etc", "cvs_check.gprep")
