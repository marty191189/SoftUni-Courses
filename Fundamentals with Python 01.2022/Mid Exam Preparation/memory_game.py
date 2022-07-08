import math


def check_for_cheating(index1, index2, boolean):

    if index1 == index2:
        boolean = True

    if index1 not in range(0, len(numbers_list)) and index2 not in range(0, len(numbers_list)):
        boolean = True

    elif index1 not in range(0, len(numbers_list)) or index2 not in range(0, len(numbers_list)):
        boolean = True

    return boolean


def add_cheat_symbol(moves, num_list):

    middle_index = math.floor(len(num_list) / 2)

    cheat_symbol = f"-{moves}a"

    num_list.insert(middle_index, cheat_symbol)
    num_list.insert(middle_index + 1, cheat_symbol)


numbers_list = input().split()

number_of_moves = 0

twin_counter = 0

you_are_cheating = False

command = input()

while not command == "end":

    number_of_moves += 1

    data = command.split()

    index_1 = int(data[0])
    index_2 = int(data[1])

    you_are_cheating = check_for_cheating(index_1, index_2, you_are_cheating)

    if you_are_cheating:

        print("Invalid input! Adding additional elements to the board")

        add_cheat_symbol(number_of_moves, numbers_list)

        you_are_cheating = False

    else:

        if numbers_list[index_1] == numbers_list[index_2]:

            print(f"Congrats! You have found matching elements - {numbers_list[index_1]}!")

            if index_2 > index_1:
                numbers_list.pop(index_2)
                numbers_list.pop(index_1)

            elif index_1 > index_2:
                numbers_list.pop(index_1)
                numbers_list.pop(index_2)

        elif not numbers_list[index_1] == numbers_list[index_2]:
            print("Try again!")

        if not numbers_list:
            print(f"You have won in {number_of_moves} turns!")
            break

    command = input()

if numbers_list:

    for el in numbers_list:

        current_count = numbers_list.count(el)

        if current_count >= 2:
            twin_counter += 1
            break

    if twin_counter > 0:

        print("Sorry you lose :(")

        numbers_list_str = [str(el) for el in numbers_list]

        print(" ".join(numbers_list_str))

    elif twin_counter == 0:
        print(f"You have won in {number_of_moves} turns!")
