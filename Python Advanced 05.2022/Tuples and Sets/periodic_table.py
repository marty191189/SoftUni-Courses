number_of_lines = int(input())

unique_set = set()

for line in range(1, number_of_lines + 1):
    current_chemical_compounds_list = input().split()

    for el in current_chemical_compounds_list:
        unique_set.add(el)

print("\n".join(unique_set))
