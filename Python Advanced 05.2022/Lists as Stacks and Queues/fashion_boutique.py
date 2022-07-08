clothes_stack = [int(el) for el in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
counter_racks = 1

while clothes_stack:

    piece_of_clothing = clothes_stack[-1]

    if piece_of_clothing > current_rack_capacity:
        current_rack_capacity = rack_capacity
        counter_racks += 1

    elif piece_of_clothing <= current_rack_capacity:
        current_rack_capacity -= piece_of_clothing
        clothes_stack.pop()

print(counter_racks)
