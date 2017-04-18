import os


def get_prefix_dir():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(this_dir)
    return root_dir


def get_config_default_filename():
    return os.path.join(get_prefix_dir(), 'etc', 'asc_config.yaml')


def get_ada_preprocessing_filename():
    return os.path.join(get_prefix_dir(), 'etc', 'cvs_check.gprep')
