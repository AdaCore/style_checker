import re


buf = "0123456789"
match = re.search("34", buf)
if match is not None:
    print(buf[match.end(0) :])
