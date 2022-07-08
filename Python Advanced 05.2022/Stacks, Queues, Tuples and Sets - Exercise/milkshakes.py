from collections import deque

chocolates_stack = [int(el) for el in input().split(", ")]
cups_deque = deque([int(el) for el in input().split(", ")])

prepared_milkshakes = 0

five_milkshakes = False

while chocolates_stack and cups_deque:

    if prepared_milkshakes >= 5:
        five_milkshakes = True
        break

    current_chocolate = chocolates_stack[-1]
    current_cup = cups_deque[0]

    if current_chocolate > 0 and current_cup > 0:

        if current_chocolate == current_cup:
            prepared_milkshakes += 1
            chocolates_stack.pop()
            cups_deque.popleft()

        else:
            temp_cup = cups_deque.popleft()
            cups_deque.append(temp_cup)

            temp_chocolate = chocolates_stack.pop()
            temp_chocolate -= 5
            chocolates_stack.append(temp_chocolate)

    else:
        if current_chocolate <= 0:
            chocolates_stack.pop()

        if current_cup <= 0:
            cups_deque.popleft()

    if prepared_milkshakes >= 5:
        five_milkshakes = True
        break

if five_milkshakes:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates_stack:
    chocolates_stack_as_str = [str(el) for el in chocolates_stack]
    print(f"Chocolate: {', '.join(chocolates_stack_as_str)}")
else:
    print("Chocolate: empty")

if cups_deque:
    cups_deque_list = [str(el) for el in cups_deque]
    print(f"Milk: {', '.join(cups_deque_list)}")
else:
    print("Milk: empty")
