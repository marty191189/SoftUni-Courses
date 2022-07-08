def even_odd(*args):

    filtered_list = []

    command = args[-1]

    if command == "even":
        for index in range(0, len(args) - 1):
            if args[index] % 2 == 0:
                filtered_list.append(args[index])

    elif command == "odd":
        for index in range(0, len(args) - 1):
            if not args[index] % 2 == 0:
                filtered_list.append(args[index])

    return filtered_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
