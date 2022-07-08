numbers = input().split(" ")
rounded_numbers_list = []


def rounding_numbers():

    for num in numbers:
        current_number = float(num)
        rounded_number = round(current_number)
        rounded_numbers_list.append(rounded_number)

    return rounded_numbers_list


print(rounding_numbers())

# без функция

# numbers = input().split(" ")
# rounded_numbers_list = []
#
# for num in numbers:
#     current_number = float(num)
#     rounded_number = round(current_number)
#     rounded_numbers_list.append(rounded_number)
#
# print(rounded_numbers_list)
