counter_coffee = 0

command = input()

while command != "END":

    if command == "coding":
        counter_coffee += 1

    elif command == "dog":
        counter_coffee += 1

    elif command == "cat":
        counter_coffee += 1

    elif command == "movie":
        counter_coffee += 1

    elif command == "CODING":
        counter_coffee += 2

    elif command == "DOG":
        counter_coffee += 2

    elif command == "CAT":
        counter_coffee += 2

    elif command == "MOVIE":
        counter_coffee += 2

    command = input()

if 5 < counter_coffee:
    print("You need extra sleep")
else:
    print(counter_coffee)

# втори начин

# lower_case_list = ["coding", "dog", "cat", "movie"]
# upper_case_list = ["CODING", "DOG", "CAT", "MOVIE"]
#
# counter_coffee = 0
#
# command = input()
#
# while command != "END":
#
#     if command in lower_case_list:
#         counter_coffee += 1
#
#     elif command in upper_case_list:
#         counter_coffee += 2
#
#     command = input()
#
# if 5 < counter_coffee:
#     print("You need extra sleep")
# else:
#     print(counter_coffee)
