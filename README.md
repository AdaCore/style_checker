Introduction
============

This is the AdaCore Style Checker (ASC). It provides a small program
called style_checker whose purpose is to first identify the type of
file being checked based on the file's extension, and then apply
a number of style checks dependent on the type of file being checked.

The program is designed to be easily callable from git or SVN hooks
to validate changes at time of commit or push. It is therefore
intentionally agnostic of any version control system.

Usage
=====

The simplest way to use this tool is to call with a module name, and
a list of files belonging to that module that need to be checked.

For instance:

    $ style_checker module file1.py file2.ads

By convention, the name of the module is typically the name of
the repository containing the files being checked. But it can be
any arbitrary name. It just needs to remain consistent, asi
this module name, as it used to read the `etc/asc_config.yaml`
configuration file to check for module-specific configuration.

Another option for calling the style checker is to pass
the list of files via stdin, instead of via the command line.
This mode is mostly there to avoid any system limitation while
trying to call this script with a large number of files. This is
very useful in the context of version control hooks, where it
can save a significant amount of time calling the style_checker
once for all files, rather than once per file.

For more information on how to use the style_checker, see the output
of

    $ style_checker --help

The AdaCore Style Checker configuration files
=============================================

The System Configuration File
-----------------------------

The AdaCore Style Checker starts by reading a system configuration
file, which provides a default configuration for all the modules
using this style checker.

By default, this system configuration is located in...

    <prefix>/etc/asc_config.yaml

... where `<prefix>` is the location where the Style Checker
was installed.

This configuration file is a YaML file. When loaded, the Style
Checker first processes the special section named `'*'`.

Once this section is processed, it looks for a section whose name
is the same as the name of the module passed on the command-line;
if found, the Style_Checker processes this section as well.

*Note that handling of module-specific sections in the system
configuration file is now deprecated, in favor of module-specific
configuration files (see below). We are planning on removing this
feature soon. This will allow us to remove the need for the special
section `'*'`, and thus have the exact same syntax for both
the system configuration file, and the module-specific configuration
file.*

The Module-Specific Configuration File
--------------------------------------

For modules that need a Style Checker with options that deviate
from the default (system) configuration, a command-line option
(`--config`) tells `style_checker` to load this file after the
system configuration file has been loaded. Eg:

    $ style_checker --config module_asc_config.yaml module file.py

The configuration provided by the module-specific config file is
applied on top of the system configuration, meaning that it does
not need to repeat the default configuration.

This configuration file is also a YaML file, and its contents follows
the same principles as in the system configuration file.

Configuration File Syntax
-------------------------

### Disabling Specific Style Checker "Rules"

The Style Checker provides support for checking a number of "rules"
(Eg: copyright headers, end-of-line characters, trailing spaces).
The Style Checker is set up to use a sub-set of those rules which
depends on the type of file (Ada, Python, Shell, etc) being checked.
You can check which rules are being checked for each type of file
using the `--dump-checks` command-line option.

If one or more of those rules do not apply to a given module,
create a section called `style_checks` in the module's configuration
file. This section should contain a list of the checks that should
be disabled. The name of the check to be disabled can be found
in the output of `--dump-checks` (see the "Legend:" section at
the bottom), and should be preceded with the character `-` (minus).

For instance, to disable copyright header checks and end-of-line
checks, create the following section in your module-specific
configuration file:

    style_checks:
        - -copyright
        - -eol

### Ada-Specific Options

Part of the Style Checks performed when checking Ada files are done
by using the GNAT compiler. How the compiler gets called can be
adjusted for each project by adding one or more of the following
entries in the `style_checks` section.

For instance, to call the GNAT compiler in Ada 95 module and with
the `-gnatX` option, your `style_checks` section should look like
this:

    style_checks:
        - gnat95
        - gnatx

Below are the different configuration options that can be used:

* **`gnatx`** (compile the code with `-gnatX`)
* **`gnat95`** (compile the code with `-gnat95`; the default is `-gnat12`)
* **`gnat05`** (compile the code with `-gnat05`; the default is `-gnat12`)

### Copyright Header Configuration

The default configuration for the copyright header checks can
be found in the system configuration file under the
`copyright_header_info` section (a dictionary). It is configured
to expect copyright headers following the AdaCore conventions.

You can either change the default configuration entirely, expand
from it, or anything in between. For this, just create a
`copyright_header_info` section in the module-specific configuration
file, and use the same options as in the system configuration file.

For configuration options which are lists, you can prepend them
with a `'+'`, which indicates that we are *adding* to the system
configuration. For instance, the following exerpt indicates that
the "format_help" configuration consists of the format_help
default loaded from the system configuration file, to which
we are adding the following two new alternatives:

    copyright_header_info:
        +format_help:
            # EPL with a single year...
            - 'Copyright (c) %(year)d '
            # EPL with a range of years year...
            - 'Copyright (c) 2014, %(year)d '

The following configuration options are supported:

* **`max_lines`** *[int]*:
  The maximum number of lines after which the Style Checker stops
  looking for a valid copyright header.

* **`holders`** [list]:
  A list of valid copyright holders. Each entry is one possible
  acceptable copyright holder.

* **`present_re`** [list]:
  A list of regular expressions detecting what looks like a copyright
  line. Each entry is one alternative of a possible copyright line

  That copyright line may or may not be correctly formed; each
  regular expression is only used as a way to perform preliminary
  detection of lines that might contain a copyright header.

* **`copyright_re`** [list]:
  A list of regular expressions matching a correctly formed copyright
  line. Each entry is one alternative of a valid copyright line.

  Please refer to the system configuration file for a description
  of the format of those regular expressions, and in particular
  of some of the assumptions made by the Style Checker (used to
  help extract some of the information from the copyright line).

* **`format_help`** [list]:
  A list of template strings telling the user what format the copyright
  line should follow. These strings are there to help the user write
  a correctly formed copyright holder by providing templates of what
  the copyright line should look like when the copyright line that
  he used was not valid.

  Please refer to the system configuration file for a description
  of the format of those strings.

