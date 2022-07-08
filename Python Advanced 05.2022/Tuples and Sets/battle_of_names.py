number_of_lines = int(input())

even_set = set()
odd_set = set()

current_ascii_sum = 0

integer_divide = 0

for line in range(1, number_of_lines + 1):
    current_name = input()

    for letter in current_name:
        current_ascii_sum += ord(letter)

    current_integer_divide = int(current_ascii_sum / line)

    if current_integer_divide % 2 == 0:
        even_set.add(current_integer_divide)

    else:
        odd_set.add(current_integer_divide)

    current_ascii_sum = 0
    current_integer_divide = 0

if sum(odd_set) == sum(even_set):
    odd_set_as_str = {str(el) for el in odd_set}
    even_set_as_str = {str(el) for el in even_set}
    print(', '.join(odd_set_as_str.union(even_set_as_str)))

elif sum(odd_set) > sum(even_set):
    odd_set_as_str = {str(el) for el in odd_set}
    even_set_as_str = {str(el) for el in even_set}
    print(', '.join(odd_set_as_str.difference(even_set_as_str)))

elif sum(odd_set) < sum(even_set):
    odd_set_as_str = {str(el) for el in odd_set}
    even_set_as_str = {str(el) for el in even_set}
    print(', '.join(odd_set_as_str.symmetric_difference(even_set_as_str)))

# по-кратко
#
# result = None
#
# if sum(odd_set) == sum(even_set):
#     result = odd_set.union(even_set)
#
# elif sum(odd_set) > sum(even_set):
#     result = odd_set.difference(even_set)
#
# elif sum(odd_set) < sum(even_set):
#     result = odd_set.symmetric_difference(even_set)
#
# print(*result, sep=', ')
