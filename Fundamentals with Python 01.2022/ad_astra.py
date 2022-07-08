import re

text = input()

pattern = r"\#([a-z A-Z]+)\#(\d{2}/\d{2}/\d{2})\#(\d+)\#|\|([a-z A-Z]+)\|(\d{2}/\d{2}/\d{2})\|(\d+)\|"

result = re.findall(pattern, text)

items = []

total_sum_calories = 0

for item in result:

    current_item = [el for el in item if el != '']

    items.append(current_item)

    total_sum_calories += int(current_item[2])

number_of_days = int(total_sum_calories / 2000)

print(f"You have food to last you for: {number_of_days} days!")

for data in items:
    item = data[0]
    date = data[1]
    current_calories = data[2]
    print(f"Item: {item}, Best before: {date}, Nutrition: {current_calories}")
