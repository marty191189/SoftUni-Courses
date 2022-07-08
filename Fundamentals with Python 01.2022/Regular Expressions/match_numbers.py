import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
text = input()

valid_nums = re.finditer(pattern, text)
valid_nums = [num.group() for num in valid_nums]

print(*valid_nums)
