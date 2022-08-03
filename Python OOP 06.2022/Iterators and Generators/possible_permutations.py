from itertools import permutations


def possible_permutations(numbers_list):

    for el in permutations(numbers_list):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]

print()

[print(n) for n in possible_permutations([1])]
