from functools import reduce


def operate(operator, *args):

    result = None

    if operator == "+":
        result = reduce(lambda x, y: x + y, args)

    elif operator == "-":
        result = reduce(lambda x, y: x - y, args)

    elif operator == "*":
        result = reduce(lambda x, y: x * y, args)

    elif operator == "/":
        try:
            result = reduce(lambda x, y: x / y, args)
        except ZeroDivisionError:
            return

    return result


print(operate("+", 1, 2, 3))

print(operate("/", 3, 0))
