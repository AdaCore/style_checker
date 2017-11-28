"""The style_checker configuration

For the most part, the style_checker's behavior is configured via
a configuration file, and optionally adjusted through the use of
command-line switches. The implementation below is based on
the organization of the config file (in YaML format), which is
described in the configuration file itself.
"""

import yaml

from asclib import get_ada_preprocessing_filename

# The name of the section in the config file which applies to any
# and all module.
ANY_MODULE_NAME = '*'

# The name of the sub-section where the list of valid copyright holders
# is specified.
COPYRIGHT_CONFIG = 'copyright'

# The name of the section specifying the list of checks that should be
# enabled/disabled.
OPTIONS_CONFIG = 'style_checks'


class Config(object):
    """A Config object, with all the configuration attributes.

    :ivar ada_preprocessing_filename: The full path to the file used
        ada_preprocessing_filename: The full path to the file used
        by the Ada files checker and passed to the compiler via
        the -gnatep switch.
    :ivar module_name: The name of the module.
    :ivar current_year: The current year.
    :ivar copyright_holders: A list of strings, each string being
        a regular expression matching a valid copyright holder name.
    :ivar options: A list of style_checks options obtained. They are
        mostly the result of parsing the config file.
    """
    def __init__(self, system_config_filename, module_name, current_year):
        """The constructor.

        :param system_config_filename: The name of the system config file.
        :type system_config_filename: str
        :param module_name: The name of the module holding the files
            we are performing the style checks on.
        :type module_name: str
        :current_year: The current year.
        :type current_year: int
        """
        self.ada_preprocessing_filename = get_ada_preprocessing_filename()
        self.module_name = module_name
        self.current_year = current_year
        self.copyright_holders = []
        self.copyright_header_info = {}
        self.options = []

        self.__read_config_file(system_config_filename)

    def __read_config_file(self, system_config_filename):
        """Read the config file and update our config accordingly.

        See the config file itself for more info on how the file
        is structured (etc/asc_config.yaml).

        :param system_config_filename: See __init__.
        :type system_config_filename: str
        """
        with open(system_config_filename) as f:
            c = yaml.load(f)

        system_config = c[ANY_MODULE_NAME] if ANY_MODULE_NAME in c else None
        module_config = c[self.module_name] if self.module_name in c else None

        # Process all known options from the config file we just
        # loaded.

        for (opt_name, opt_list) in (
                (COPYRIGHT_CONFIG, self.copyright_holders),
                (OPTIONS_CONFIG, self.options)):
            # Get the option value, giving priority to the module-specific
            # section.
            if module_config is not None and opt_name in module_config:
                opt_list[:] = module_config[opt_name]
            elif system_config is not None and opt_name in system_config:
                opt_list[:] = system_config[opt_name]

            # See if there an entry in the module-specific section whose
            # name is opt_name with a '+' ahead of it. Those are requests
            # to append to the config, rather than to override it.
            if module_config is not None and '+' + opt_name in module_config:
                opt_list.extend(module_config['+' + opt_name])

        self.copyright_header_info = \
            system_config['copyright_header_info']
        if module_config is not None and \
                'copyright_header_info' in module_config:
            # Override part or all of the default configuration with
            # the repository-specific config.
            self.copyright_header_info.update(
                module_config['copyright_header_info'])
            # Also, because yaml does not provide automatic merging
            # for lists (only dictionaries), so we provide an alternative
            # way to do so where keys whose name start with a '+' means
            # append the list to the list from the key without the '+'.
            for key in self.copyright_header_info.keys():
                if key.startswith('+'):
                    self.copyright_header_info[key[1:]].extend(
                        self.copyright_header_info[key])
                    del self.copyright_header_info[key]
