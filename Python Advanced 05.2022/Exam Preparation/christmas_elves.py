from collections import deque

elf_energy_deque = deque([int(el) for el in input().split()])
boxes_stack = [int(el) for el in input().split()]

toys = 0
energy = 0

counter_elves = 0

while elf_energy_deque and boxes_stack:

    while elf_energy_deque and elf_energy_deque[0] < 5:
        elf_energy_deque.popleft()

    if not elf_energy_deque:
        break

    current_elf = elf_energy_deque.popleft()
    current_box = boxes_stack.pop()

    counter_elves += 1

    if counter_elves % 3 == 0 and counter_elves % 5 == 0:

        if current_elf < current_box * 2:
            current_elf = current_elf * 2
            elf_energy_deque.append(current_elf)
            boxes_stack.append(current_box)

        elif current_elf >= current_box * 2:
            double_box = current_box * 2
            energy += double_box
            current_elf -= double_box
            elf_energy_deque.append(current_elf)

    elif counter_elves % 5 == 0:

        if current_elf < current_box:
            current_elf = current_elf * 2
            elf_energy_deque.append(current_elf)
            boxes_stack.append(current_box)

        elif current_elf >= current_box:
            energy += current_box
            current_elf -= current_box
            elf_energy_deque.append(current_elf)

    elif counter_elves % 3 == 0:

        if current_elf < current_box * 2:
            current_elf = current_elf * 2
            elf_energy_deque.append(current_elf)
            boxes_stack.append(current_box)

        elif current_elf >= current_box * 2:
            toys += 2
            double_box = current_box * 2
            energy += double_box
            current_elf -= double_box
            current_elf += 1
            elf_energy_deque.append(current_elf)

    else:

        if current_elf < current_box:
            current_elf = current_elf * 2
            elf_energy_deque.append(current_elf)
            boxes_stack.append(current_box)

        elif current_elf >= current_box:
            toys += 1
            energy += current_box
            current_elf -= current_box
            current_elf += 1
            elf_energy_deque.append(current_elf)

print(f"Toys: {toys}")
print(f"Energy: {energy}")

if elf_energy_deque:
    print(f"Elves left: {', '.join([str(el) for el in elf_energy_deque])}")

if boxes_stack:
    print(f"Boxes left: {', '.join([str(el) for el in boxes_stack])}")


# втори начин

# from collections import deque
#
# elf_energy_deque = deque([int(el) for el in input().split()])
# boxes_stack = [int(el) for el in input().split()]
#
# toys = 0
# energy = 0
# counter_elves = 0
#
# while elf_energy_deque and boxes_stack:
#
#     while elf_energy_deque and elf_energy_deque[0] < 5:
#         elf_energy_deque.popleft()
#
#     if not elf_energy_deque:
#         break
#
#     current_elf = elf_energy_deque.popleft()
#     current_box = boxes_stack.pop()
#
#     counter_elves += 1
#
#     toys_to_be_created_count = 1
#     energy_to_be_spent = current_box
#     energy_increase_factory = 1
#
#     if counter_elves % 3 == 0:
#         toys_to_be_created_count = 2
#         energy_to_be_spent *= 2
#
#     if counter_elves % 5 == 0:
#         toys_to_be_created_count = 0
#         energy_increase_factory = 0
#
#     if energy_to_be_spent <= current_elf:
#         toys += toys_to_be_created_count
#         energy += energy_to_be_spent
#         elf_energy_deque.append((current_elf - energy_to_be_spent) + energy_increase_factory)
#
#     else:
#         boxes_stack.append(current_box)
#         elf_energy_deque.append(current_elf * 2)
#
# print(f"Toys: {toys}")
# print(f"Energy: {energy}")
#
# if elf_energy_deque:
#     print(f"Elves left: {', '.join([str(el) for el in elf_energy_deque])}")
#
# if boxes_stack:
#     print(f"Boxes left: {', '.join([str(el) for el in boxes_stack])}")
