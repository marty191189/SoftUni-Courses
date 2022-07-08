number_of_codes = int(input())

guests_set = set()

for number in range(1, number_of_codes + 1):
    current_code = input()
    guests_set.add(current_code)

guests_code = input()

while not guests_code == "END":
    guests_set.remove(guests_code)
    guests_code = input()

print(len(guests_set))
print("\n".join(sorted(guests_set)))
