import re

pattern = r"(^|(?<=\s))(?P<user>[a-z0-9]+[\._-]?[a-z0-9]+?)@(?P<host>([a-z0-9]+[\._-])+[a-z0-9]+)"

text = input()

valid_emails = [el.group() for el in re.finditer(pattern, text)]

print(*valid_emails, sep="\n")
