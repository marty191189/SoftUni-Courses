import re

text = input()

pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"

valid_links_list = []

while text:
    valid_links = [el.group() for el in re.finditer(pattern, text)]

    if valid_links:
        valid_links_list.extend(valid_links)

    text = input()

print(*valid_links_list, sep="\n")
