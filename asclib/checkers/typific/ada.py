import os
import re

from asclib.checkers.typific import TypificChecker, TypificCheckerInfo
from asclib.ex import command_line_image, Run
from asclib.logging import log_info


RT_SPEC = 'Ada Runtime spec'
RT_BODY = 'Ada Runtime body'
COMPILER_CORE = 'compiler Ada file'
STD_ADA = 'regular Ada file'

RT_SPEC_PATTERN = r'^[agis]-[a-z0-9-_]+\.ads$'
RT_BODY_PATTERN = r'^[agis]-[a-z0-9-_]+\.adb$'
ADA83_RT_SPEC_PATTERN = ('^(' +
                         '|'.join(['unch(conv|deal)',
                                   '(sequen|direct|text_)io',
                                   'ioexcept',
                                   'calendar',
                                   'machcode']) +
                         r')\.ads$')


class AdaFileChecker(TypificChecker):
    rulific_decision_map = {
        'copyright': True,
        'eol': True,
        'first_line_comment': True,
        'max_line_length': False,
        'no_dos_eol': True,
        'no_last_eol': True,
        'no_rcs_keywords': True,
        'no_tab_indent': False,
        'no_trailing_space': True,
        }

    @property
    def typific_info(self):
        return TypificCheckerInfo(
            comment_line_re='--*$',
            ada_RM_spec_p=(self.file_type == RT_SPEC),
            copyright_box_r_edge_re=None)

    @property
    def file_type(self):
        if self.__is_GNAT_module():
            basename = os.path.basename(self.filename)
            if re.match(RT_SPEC_PATTERN, basename) is not None:
                return RT_SPEC
            elif re.match(ADA83_RT_SPEC_PATTERN, basename) is not None:
                return RT_SPEC
            elif re.match(RT_BODY_PATTERN, basename) is not None:
                return RT_BODY
            else:
                return COMPILER_CORE
        else:
            return STD_ADA

    def run_external_checker(self):
        file_type = self.file_type

        cmd = ['gcc',
               '-c',
               '-gnats',
               '-gnatm20',
               # Set "-x ada" so that we can style check Ada sources even
               # if their extension is not automatically identified by GCC.
               '-x', 'ada',
               ]

        # Base options: use GNAT style

        if file_type in (RT_SPEC, RT_BODY):
            # Set GNAT mode for runtime files only (changes legality and
            # semantics, and sets more restrictive style rules).
            # Note: This also enables language extensions.
            cmd.append('-gnatg')
        else:
            # Enable GNAT style checks, GNAT warnings, and treat warnings
            # and style messages as errors.
            cmd.extend(['-gnatyg',
                        '-gnatw.g',
                        '-gnatwe'])

        # The "gnat" repository needs specific treatment because we want
        # to allow building GNAT without requiring too recent a compiler.

        if file_type in (RT_SPEC, RT_BODY):
            # Language version already set by -gnatg for runtime units
            pass
        elif file_type == COMPILER_CORE:
            cmd.append('-gnat12')

        # For all other repositories, allow Ada 2012 by default, except
        # explicity overriden by the repository.

        elif 'gnatx' in self.config.style_checks_options:
            cmd.append('-gnatX')
        elif 'gnat95' in self.config.style_checks_options:
            cmd.append('-gnat95')
        elif 'gnat05' in self.config.style_checks_options:
            cmd.append('-gnat05')
        else:
            cmd.append('-gnat12')

        # Set preprocessing data file.
        cmd.append('-gnatep=' + self.config.ada_preprocessing_filename)

        cmd.append(self.filename)

        # Run GCC with some some critical environment variables unset.
        BANNED_ENV_VARS = ('GCC_EXEC_PREFIX', 'GCC_INSTALL_DIRECTORY',
                           'GCC_INCLUDE_DIR',
                           'GCC_ROOT', 'GNAT_ROOT', 'BINUTILS_ROOT')
        gcc_env = {var_name: value for var_name, value in os.environ.items()
                   if var_name not in BANNED_ENV_VARS}

        try:
            log_info('Running: %s' % command_line_image(cmd), 2)
            p = Run(cmd, env=gcc_env)
            if p.status != 0 or p.out:
                return p.out
        except OSError as e:
            return 'Failed to run %s: %s' % (cmd[0], e)

    def __is_GNAT_module(self):
        return self.config.module_name in ('gnat', 'ada')
