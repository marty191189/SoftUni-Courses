from itertools import chain

from collections import deque

materials_stack = [int(el) for el in input().split()]
magic_values_deque = deque([int(el) for el in input().split()])

total_magic_level = None

pair_crafted = False

toys_crafted_list = []

toys_dict = {}

while materials_stack and magic_values_deque:

    current_material = materials_stack[-1]
    current_magic = magic_values_deque[0]

    if current_material == 0 and current_magic == 0:
        materials_stack.pop()
        magic_values_deque.popleft()

    elif current_material == 0:
        materials_stack.pop()

    elif current_magic == 0:
        magic_values_deque.popleft()

    total_magic_level = current_material * current_magic

    positive_range = chain(range(1, 150), range(151, 250), range(251, 300), range(301, 400))

    if total_magic_level in positive_range:
        magic_values_deque.popleft()
        materials_stack[-1] += 15

    elif total_magic_level < 0:
        result = current_material + current_magic
        materials_stack.pop()
        magic_values_deque.popleft()
        materials_stack.append(result)

    elif total_magic_level == 150:
        toy = "Doll"
        if toy not in toys_dict:
            toys_dict[toy] = 1
        else:
            toys_dict[toy] += 1
        materials_stack.pop()
        magic_values_deque.popleft()

    elif total_magic_level == 250:
        toy = "Wooden train"
        if toy not in toys_dict:
            toys_dict[toy] = 1
        else:
            toys_dict[toy] += 1
        materials_stack.pop()
        magic_values_deque.popleft()

    elif total_magic_level == 300:
        toy = "Teddy bear"
        if toy not in toys_dict:
            toys_dict[toy] = 1
        else:
            toys_dict[toy] += 1
        materials_stack.pop()
        magic_values_deque.popleft()

    elif total_magic_level == 400:
        toy = "Bicycle"
        if toy not in toys_dict:
            toys_dict[toy] = 1
        else:
            toys_dict[toy] += 1
        materials_stack.pop()
        magic_values_deque.popleft()

if "Doll" in toys_dict and "Wooden train" in toys_dict:
    pair_crafted = True

if "Teddy bear" in toys_dict and "Bicycle" in toys_dict:
    pair_crafted = True

if pair_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stack:
    materials_stack_list = [str(el) for el in materials_stack]
    materials_stack_list.reverse()
    print(f"Materials left: {', '.join(materials_stack_list)}")

if magic_values_deque:
    magic_values_deque_list = [str(el) for el in magic_values_deque]
    print(f"Magic left: {', '.join(magic_values_deque_list)}")

sorted_toys_dict = sorted(toys_dict.items(), key=lambda x: x[0])

for toy, counter in sorted_toys_dict:
    print(f"{toy}: {counter}")
