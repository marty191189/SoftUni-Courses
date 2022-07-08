import math
from collections import deque

expression = input().split()

my_deque = deque()

first_number = None

for el in expression:

    if el == "+":
        first_number = my_deque.popleft()
        while my_deque:
            current_number = my_deque.popleft()
            first_number += current_number
        my_deque.append(first_number)

    elif el == "-":
        first_number = my_deque.popleft()
        while my_deque:
            current_number = my_deque.popleft()
            first_number -= current_number
        my_deque.append(first_number)

    elif el == "*":
        first_number = my_deque.popleft()
        while my_deque:
            current_number = my_deque.popleft()
            first_number *= current_number
        my_deque.append(first_number)

    elif el == "/":
        first_number = my_deque.popleft()
        while my_deque:
            current_number = my_deque.popleft()
            first_number = math.floor(first_number / current_number)
        my_deque.append(first_number)

    else:
        my_deque.append(int(el))

print(first_number)
