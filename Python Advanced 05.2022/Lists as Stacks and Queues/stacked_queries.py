number_of_queries = int(input())

number_stack = []

for number in range(1, number_of_queries + 1):

    current_query = [int(number) for number in input().split()]

    command = current_query[0]

    if command == 1:
        number = current_query[1]
        number_stack.append(number)

    elif command == 2 and number_stack:
        number_stack.pop()

    elif command == 3 and number_stack:
        max_number = max(number_stack)
        print(max_number)

    elif command == 4 and number_stack:
        min_number = min(number_stack)
        print(min_number)

reversed_stack = []

while number_stack:
    reversed_stack.append(str(number_stack.pop()))

print(", ".join(reversed_stack))
