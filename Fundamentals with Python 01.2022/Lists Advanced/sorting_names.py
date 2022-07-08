names = input().split(", ")

sorted_names_a_to_z = sorted(names)

sorted_names_a_to_z_descending = sorted(sorted_names_a_to_z, key=lambda name: -len(name))

print(sorted_names_a_to_z_descending)
