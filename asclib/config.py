import yaml

from asclib import get_ada_preprocessing_filename

ANY_MODULE_NAME = '*'

COPYRIGHT_CONFIG = 'copyright'
OPTIONS_CONFIG = 'style_checks'


class Config(object):
    def __init__(self, config_filename, module_name, current_year):
        self.ada_preprocessing_filename = get_ada_preprocessing_filename()
        self.module_name = module_name
        self.current_year = current_year
        self.copyright_holders = []
        self.options = []

        self.__read_config_file(config_filename)

    def __read_config_file(self, config_filename):
        """Read the config file and update our config accordingly.

        See the config file itself for more info on how the file
        is structured (etc/asc_config.yaml).
        """
        with open(config_filename) as f:
            c = yaml.load(f)

        # Process all known options from the config file we just
        # loaded.

        for (opt_name, opt_list) in (
                (COPYRIGHT_CONFIG, self.copyright_holders),
                (OPTIONS_CONFIG, self.options)):
            # Get the option value, giving priority to the module-specific
            # section.
            if self.module_name in c and opt_name in c[self.module_name]:
                opt_list[:] = c[self.module_name][opt_name]
            elif ANY_MODULE_NAME in c and opt_name in c[ANY_MODULE_NAME]:
                opt_list[:] = c[ANY_MODULE_NAME][opt_name]

            # See if there an entry in the module-specific section whose
            # name is opt_name with a '+' ahead of it. Those are requests
            # to append to the config, rather than to override it.
            if self.module_name in c and '+' + opt_name in c[self.module_name]:
                opt_list.extend(c[self.module_name]['+' + opt_name])
