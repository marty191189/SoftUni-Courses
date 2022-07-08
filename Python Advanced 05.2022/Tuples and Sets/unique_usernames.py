number_of_usernames = int(input())

usernames_set = set()

for number in range(1, number_of_usernames + 1):
    current_username = input()
    usernames_set.add(current_username)

print("\n".join(usernames_set))
