number_of_names = int(input())

names_set = set()

for number in range(1, number_of_names + 1):
    current_name = input()
    names_set.add(current_name)

print('\n'.join(names_set))
