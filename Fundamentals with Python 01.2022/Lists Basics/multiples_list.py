factor = int(input())
number = int(input())

list_of_numbers = []

for i in range(1, number + 1):

    current_number = factor * i

    list_of_numbers.append(current_number)

print(list_of_numbers)

# втори начин
#
# num_1 = int(input())
# num_2 = int(input())
#
# new_list = []
#
# for num in range(1, num_2 + 1):
#     new_list.append(num * num_1)
#
# print(new_list)
