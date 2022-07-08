import re

text = input()
regex = r"(?P<delimiter>[=//])([A-Z][A-Za-z]{2,})(?P=delimiter)"

matches = re.finditer(regex, text)
locations = list()
points = 0

for match in matches:
    city = match[2]
    locations.append(city)
    points += len(city)

output_locations = ", ".join(locations)
print(f"Destinations: {output_locations}")
print(f"Travel Points: {points}")
