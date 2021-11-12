from asclib.checkers.rulific import AbstractRuleChecker

CHARACTERS_NOT_ALLOWED = (
    # Characters that an attacker could use to exploit the Unicode
    # Bidi algorithm to construct source code that would appear
    # innocuous when rendered in an editor, but that would actually
    # contain malicious code that a compiler would compile.
    "\u202A",  # Left-To-Right Embedding
    "\u202B",  # Right-To-Left Embedding
    "\u202C",  # Pop Directional Formatting
    "\u202D",  # Left-To-Right Override
    "\u202E",  # Right-To-Left Override
    "\u2066",  # Left-To-Right Isolate
    "\u2067",  # Right-To-Left Isolate
    "\u2068",  # First Strong Isolate
    "\u2069",  # Pop Directional Isolate
)


class BidiRuleChecker(AbstractRuleChecker):
    RULE_CONFIG_NAME = "bidi"
    RULE_DESCRIPTION = "reject characters that could be used to mask malicious code"

    def check_rule(self, lineno, line, eol):
        bad_chars = []
        for index, char in enumerate(line, start=1):
            if char in CHARACTERS_NOT_ALLOWED:
                bad_chars.append(f"{index} (U+{ord(char):X})")
        if bad_chars:
            if len(bad_chars) > 1:
                return "forbidden unicode characters at indices " + ", ".join(bad_chars)
            else:
                return f"forbidden unicode character at index {bad_chars[0]}"
