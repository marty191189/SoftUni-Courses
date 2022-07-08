class ValueCannotBeNegative(Exception):
    pass


for number in range(1, 5 + 1):
    current_number = int(input())

    if current_number < 0:
        raise ValueCannotBeNegative
