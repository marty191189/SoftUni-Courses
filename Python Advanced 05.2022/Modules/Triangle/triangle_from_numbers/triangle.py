def print_upper_part(number_1):

    for line in range(1, number_1 + 1):

        for num in range(1, line + 1):
            print(num, end=" ")
        print()


def print_bottom_part(number_1):

    for line in range(number_1 - 1, 0, -1):

        for num in range(1, line + 1):
            print(num, end=" ")
        print()


def print_triangle(number_1):

    print_upper_part(number_1)
    print_bottom_part(number_1)
