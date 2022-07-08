text = input()

my_list = text.split(" ")

list_doubles = []

for i in my_list:

    a = int(i)

    if a > 0:
        b = -a
        list_doubles.append(b)

    elif a < 0:
        b = abs(a)
        list_doubles.append(b)

    elif a == 0:
        list_doubles.append(a)

print(list_doubles)

# втори начин
#
# numbers = input().split(" ")
# new_list = []
#
# for num in numbers:
#     if int(num) > 0:
#         new_list.append(-int(num))
#     else:
#         new_list.append(abs(int(num)))
#
# print(new_list)

# трети начин
#
# numbers = [-num if num > 0 else abs(num) for num in list(map(int, input().split(" ")))]
# print(numbers)
