from collections import deque

cups_deque = deque([int(el) for el in input().split()])
bottles_stack = [int(el) for el in input().split()]
wasted_water = 0

while bottles_stack and cups_deque:

    current_bottle = bottles_stack[-1]
    current_cup = cups_deque[0]

    if current_bottle > current_cup:
        diff = current_bottle - current_cup
        wasted_water += diff
        bottles_stack.pop()
        cups_deque.popleft()

    elif current_bottle == current_cup:
        diff = current_bottle - current_cup
        wasted_water += diff
        bottles_stack.pop()
        cups_deque.popleft()

    elif current_bottle < current_cup:
        current_cup -= current_bottle
        bottles_stack.pop()
        cups_deque.popleft()
        cups_deque.insert(0, current_cup)

if not cups_deque:
    print(f"Bottles: {' '.join([str(el) for el in bottles_stack])}")

if not bottles_stack:
    print(f"Cups: {' '.join([str(el) for el in cups_deque])}")

print(f"Wasted litters of water: {wasted_water}")
