numbers_list = input().split()
numbers_list = list(map(int, numbers_list))

command = input()

while not command == "end":

    data = command.split()

    if data[0] == "swap":
        index_1 = int(data[1])
        index_2 = int(data[2])

        numbers_list[index_1], numbers_list[index_2] = numbers_list[index_2], numbers_list[index_1]

    elif data[0] == "multiply":
        index_1 = int(data[1])
        index_2 = int(data[2])

        numbers_list[index_1] *= numbers_list[index_2]

    elif data[0] == "decrease":
        numbers_list = list(map(lambda n: n - 1, numbers_list))

    command = input()

numbers_list = list(map(str, numbers_list))

print(", ".join(numbers_list))


# втори начин
#
# numbers = input().split(" ")
# numbers = list(map(int, numbers))
#
# line = input()
#
# while line != "end":
#
#     if line == "decrease":
#         numbers = list(map(lambda n: n - 1, numbers))
#
#     else:
#         data = line.split(" ")
#         command = data[0]
#         index_1 = int(data[1])
#         index_2 = int(data[2])
#
#         if command == "swap":
#             numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]
#
#         elif command == "multiply":
#             numbers[index_1] = numbers[index_1] * numbers[index_2]
#
#     line = input()
#
# numbers = list(map(str, numbers))
#
# output = ", ".join(numbers)
#
# print(output)
