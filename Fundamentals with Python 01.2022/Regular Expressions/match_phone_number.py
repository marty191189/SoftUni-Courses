# Инес + Мартин Панков
import re

pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})\b"
text = input()

matches = re.finditer(pattern, text)
valid_phones = [match.group() for match in matches]
print(", ".join(valid_phones))

# втори начин от презентацията
#
# import re
# pattern = "(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b"
# text = input()
# matches = re.findall(pattern, text)
# print(", ".join(matches))
