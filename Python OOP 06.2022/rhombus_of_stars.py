def print_row(num, row):
    for space in range(num - row):
        print(" ", end="")
    for star in range(1, row):
        print("*", end=" ")
    print("*")


def print_up(num):
    for row in range(1, num + 1):
        print_row(num, row)


def print_bottom(num):
    for row in range(num - 1, 0, -1):
        print_row(num, row)


def print_rhombus(num):
    print_up(num)
    print_bottom(num)


n = int(input())
print_rhombus(n)
