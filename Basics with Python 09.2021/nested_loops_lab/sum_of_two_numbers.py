starting_interval = int(input())
final_interval = int(input())
magic_number = int(input())
combinations = 0
condition = False

for i in range(starting_interval, final_interval + 1):
    for x in range(starting_interval, final_interval + 1):
        if i + x == magic_number:
            combinations += 1
            condition = True
            print(f"Combination N:{combinations} ({i} + {x} = {magic_number})")
            break

        if i + x != magic_number:
            combinations += 1

    if condition:
        break

if not condition:
    print(f"{combinations} combinations - neither equals {magic_number}")
