import re

lines = []

while True:

    line = input()

    if line:
        lines.append(line)

    else:
        break

text = '\n'.join(lines)

pattern = r"\d+"

result = re.findall(pattern, text)

print(" ".join(result))

# втори начин
#
# print(*result)
