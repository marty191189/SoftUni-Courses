text = input()
number = int(input())


def repeater(text_1, number_1):
    result = text_1 * number_1
    return result


print(repeater(text, number))

# втори начин

# text = input()
# number = int(input())
#
#
# result = lambda text_1, number_1: text_1 * number_1
#
#
# print(result(text, number))
