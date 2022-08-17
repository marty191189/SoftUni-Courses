from collections import deque

materials_stack = [int(el) for el in input().split()]

magic_deque = deque([int(el) for el in input().split()])

crafted_gifts_dict = {}

succeeded_in_crafting = False

while magic_deque and materials_stack:

    current_material = materials_stack.pop()
    current_magic = magic_deque.popleft()
    current_sum = current_magic + current_material

    if current_sum < 100:

        if current_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            current_sum = current_material + current_magic

        else:
            current_sum *= 2

    if 499 < current_sum:
        current_sum /= 2

    if 100 <= current_sum <= 199:

        if "Gemstone" not in crafted_gifts_dict:
            crafted_gifts_dict["Gemstone"] = 1
        else:
            crafted_gifts_dict["Gemstone"] += 1

    if 200 <= current_sum <= 299:

        if "Porcelain Sculpture" not in crafted_gifts_dict:
            crafted_gifts_dict["Porcelain Sculpture"] = 1
        else:
            crafted_gifts_dict["Porcelain Sculpture"] += 1

    if 300 <= current_sum <= 399:

        if "Gold" not in crafted_gifts_dict:
            crafted_gifts_dict["Gold"] = 1
        else:
            crafted_gifts_dict["Gold"] += 1

    if 400 <= current_sum <= 499:

        if "Diamond Jewellery" not in crafted_gifts_dict:
            crafted_gifts_dict["Diamond Jewellery"] = 1
        else:
            crafted_gifts_dict["Diamond Jewellery"] += 1


if ("Gemstone" in crafted_gifts_dict and "Porcelain Sculpture" in crafted_gifts_dict) or \
        ("Gold" in crafted_gifts_dict and "Diamond Jewellery" in crafted_gifts_dict):
    succeeded_in_crafting = True

if succeeded_in_crafting:
    print("The wedding presents are made!")

else:
    print("Aladdin does not have enough wedding presents.")

if materials_stack:
    print(f"Materials left: {', '.join([str(el) for el in materials_stack])}")

if magic_deque:
    print(f"Magic left: {', '.join([str(el) for el in magic_deque])}")

sorted_dictionary = sorted(crafted_gifts_dict.items(), key=lambda x: x[0])

for gift_name, quantity in sorted_dictionary:
    print(f"{gift_name}: {quantity}")
