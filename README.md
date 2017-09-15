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
