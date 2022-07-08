from collections import deque

text_deque = deque(input().split())

primary_colors_list = ["red", "yellow", "blue"]

secondary_colors_list = ["orange", "purple", "green"]

found_colors_list = []

while text_deque:
    first = text_deque.popleft()
    last = text_deque.pop() if text_deque else ''

    result = first + last
    reversed_result = last + first

    if result in primary_colors_list or result in secondary_colors_list:
        found_colors_list.append(result)
        continue

    if reversed_result in primary_colors_list or reversed_result in secondary_colors_list:
        found_colors_list.append(reversed_result)
        continue

    first = first[:-1]
    last = last[:-1]

    if first:
        text_deque.insert(len(text_deque) // 2, first)
    if last:
        text_deque.insert(len(text_deque) // 2, last)

result = []

forming_colors_dict = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

for color in found_colors_list:
    if color in primary_colors_list:
        result.append(color)
        continue

    is_collected = True

    for helper_color in forming_colors_dict[color]:
        if helper_color not in found_colors_list:
            is_collected = False
            break

    if is_collected:
        result.append(color)

print(result)
