from collections import deque

bees_deque = deque([int(el) for el in input().split()])
nectar_stack = [int(el) for el in input().split()]
operators_deque = deque(input().split())

total_honey = 0

operations_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

while bees_deque and nectar_stack:

    current_bee = bees_deque.popleft()
    current_nectar = nectar_stack.pop()

    if current_nectar < current_bee:
        bees_deque.appendleft(current_bee)
        continue

    if current_nectar == 0:
        continue

    operator = operators_deque.popleft()
    total_honey += abs(operations_dict[operator](current_bee, current_nectar))

print(f"Total honey made: {total_honey}")

if bees_deque:
    bees_deque_list = [str(el) for el in bees_deque]
    print(f"Bees left: {', '.join(bees_deque_list)}")

if nectar_stack:
    nectar_stack_list = [str(el) for el in nectar_stack]
    print(f"Nectar left: {', '.join(nectar_stack_list)}")
