import re

from asclib.checkers.rulific import AbstractRuleChecker

ADA_RM_SPEC_IDENTIFIER = "This specification is derived from the Ada Reference Manual"


class CopyrightRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = "copyright"
    RULE_DESCRIPTION = "check that file has a well formed copyright notice"

    def init_context_data(self):
        # Is this file identified as an Ada RM spec for which a copyright
        # is line is not necessary?
        #
        # Note that, as per a discussion under NA17-007, the special
        # identifier for these kinds of files waves the requirement
        # for a copyright line.  However, if one is present, it does
        # NOT wave the requirement for that one to actually be correctly
        # formatted.
        self.context_has_valid_ada_RM_spec_id = False

        # The first line of our file where we detected a copyright line.
        self.context_copyright_notice_lineno = 0

        # We have to buffer all the error messages, because we could
        # be finding errors only to find later on that our file
        # contains the ADA_RM_SPEC_IDENTIFIER, which tells us to stop
        # checking for copyright notices entirely.
        self.context_copyright_notice_err_msg = []

        # Have we found one correctly formatted copyright line which
        # fulfills all the requirements (location, format, year, holder,
        # etc)?
        self.context_has_valid_copyright_p = False

        # Have we found one incorrectly formatted copyright line?
        self.context_has_improperly_formatted = False

        # Some other attributes that are not strictly state variables
        # that we need to preserve, but will just act as shortcuts
        # to some configuration variables, hopefully making the code
        # shorter and easier to understand.
        cinfo = self.config.copyright_header_info
        self.copyright_holders = cinfo["holders"]
        self.max_lines_for_copyright_notice = cinfo["max_lines"]
        self.format_help = cinfo["format_help"]
        self.present_re = cinfo["present_re"]
        self.copyright_re = cinfo["copyright_re"]

    def check_rule(self, lineno, line, eol):
        if self.context_has_valid_copyright_p:
            # We have already seen and processed a valid copyright notice.
            # No need to look at any line beyond this line anymore.
            return

        if (
            lineno <= self.max_lines_for_copyright_notice
            and self.typific_info.ada_RM_spec_p
            and ADA_RM_SPEC_IDENTIFIER in line
        ):
            self.context_has_valid_ada_RM_spec_id = True
            return

        if (
            lineno > self.max_lines_for_copyright_notice
            and self.context_copyright_notice_lineno > 0
        ):
            # We're now past the portion of the file where we expect
            # to find a valid copyright file. Since we did find one
            # copyright notice, looking further wouldn't change anything
            # in terms of the outcome of the error messages we would
            # produce. So stop processing that file from now on.
            return

        # Check to see if we have a copyright line...
        # If we do, and it's the first copyright line we've seen,
        # record that line number.
        for present_re in self.present_re:
            m = re.search(present_re, line, re.I)
            if m is not None:
                break
        if m is None:
            # None of the "present_re" regular expressions matched.
            # It must not be a copyright line.
            return
        if self.context_copyright_notice_lineno == 0:
            self.context_copyright_notice_lineno = lineno

        # Make sure our copyright line is correctly formatted.
        for copyright_re in self.copyright_re:
            m = re.match(copyright_re, line)
            if m is not None:
                break
        if m is None:
            # We only emit the error message for the first improperly
            # copyright line we've seen (this seems like a sensible
            # behavior, but is also a behavior which we inherited from
            # cvs_check, the previous style checker).
            if not self.context_has_improperly_formatted:
                self.context_copyright_notice_err_msg.extend(
                    [
                        "%s:%d: Copyright notice is not correctly formatted"
                        % (self.filename, lineno),
                        "It must look like...",
                        "",
                    ]
                    + "\nor\n".join(
                        [
                            "    %s<copyright holder>"
                            % (format_help % {"year": self.config.current_year})
                            for format_help in self.format_help
                        ]
                    ).splitlines()
                    + ["", "... where <copyright holder> can be any of:"]
                    + ["    - `%s'" % holder for holder in self.copyright_holders]
                )
                self.context_has_improperly_formatted = True
            return

        actual_holder = m.group("holder")

        if self.typific_info.copyright_box_r_edge_re is not None:
            # Usually we identify the end of the copyright holder
            # name by it being the last non-blank/space/slash/start
            # on the line. However, this type of file sometimes has
            # its copyright notice boxed. For instance, in some texi
            # files, the copyright notice is boxed in 'o's. We need
            # to strip that right edge of the box, as well as the
            # spaces before that.
            h_m = re.match(
                r"(.*)%s\s*" % self.typific_info.copyright_box_r_edge_re, actual_holder
            )
            if h_m is not None:
                # Right edge of box found. Only consider the text
                # before that.
                actual_holder = h_m.group(1).rstrip()

        # If the module only allows a restricted list of possible
        # copyright holders, then check that list.
        if self.copyright_holders and actual_holder not in self.copyright_holders:
            self.context_copyright_notice_err_msg.extend(
                [
                    "%s:%d: Copyright notice has unexpected copyright holder:"
                    % (self.filename, lineno),
                    "      `%s'" % actual_holder,
                    "Expected either of:",
                ]
                + ["    - `%s'" % holder for holder in self.copyright_holders]
            )
            return

        copyright_year = m.group("year")
        if copyright_year != str(self.config.current_year):
            self.context_copyright_notice_err_msg.append(
                "%s:%d: Copyright notice must include current year"
                " (found %s, expected %s)"
                % (self.filename, lineno, copyright_year, self.config.current_year)
            )
            return

        if lineno <= self.max_lines_for_copyright_notice:
            # This copyright line answers all the requirements, and thus
            # is declared as valid.
            self.context_has_valid_copyright_p = True

    def global_check(self):
        if self.context_has_valid_copyright_p:
            # This file has a valid copyright line, and this overrides
            # any error we may have seen outside of that file.
            return

        if (
            self.context_copyright_notice_lineno == 0
            and self.context_has_valid_ada_RM_spec_id
        ):
            # There was no copyright line at all, but we identified
            # this as being an Ada RM spec for which we don't need
            # a copyright line.
            return

        if self.context_copyright_notice_lineno == 0:
            self.context_copyright_notice_err_msg.insert(
                0,
                "%s: Copyright notice missing, must occur before line %d"
                % (self.filename, self.max_lines_for_copyright_notice),
            )

        elif self.context_copyright_notice_lineno > self.max_lines_for_copyright_notice:
            # The legacy style checker (cvs_check) doesn't show
            # any formatting errors we might have found on the format
            # of the copyright notice if that copyright line was found
            # past the threshold.  Do the same here by overriding
            # self.context_copyright_notice_err_msg.
            self.context_copyright_notice_err_msg = [
                "%s:%d: Copyright notice must occur before line %d"
                % (
                    self.filename,
                    self.context_copyright_notice_lineno,
                    self.max_lines_for_copyright_notice,
                )
            ]

        return "\n".join(self.context_copyright_notice_err_msg)
