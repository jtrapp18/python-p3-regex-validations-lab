import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][A-z]+\s[A-Z][A-z'-]+|[A-Z][A-z'-]+"
name_regex = re.compile(name)

phone_number = r"\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4}|[0-9]{10}"
phone_regex = re.compile(phone_number)

email_address = r"[A-z][A-z0-9._-]+@\w+\.[a-z]+"
email_regex = re.compile(email_address)
