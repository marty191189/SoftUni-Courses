number_of_electrons = int(input())

my_list = []

for num in range(1, number_of_electrons + 1):
    element = 2 * (num ** 2)

    if element < number_of_electrons:
        number_of_electrons -= element
        my_list.append(element)

    else:
        my_list.append(number_of_electrons)
        break

print(my_list)
