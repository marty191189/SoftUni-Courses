operator = input()
number_1 = int(input())
number_2 = int(input())


def calculator(num1, num2, operator1):

    result = None

    if operator1 == "add":
        result = int(num1 + num2)

    elif operator1 == "subtract":
        result = int(num1 - num2)

    elif operator1 == "multiply":
        result = int(num1 * num2)

    elif operator1 == "divide":
        result = int(num1 / num2)

    return result


print(calculator(number_1, number_2, operator))
