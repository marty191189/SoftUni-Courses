name_first_player = input()
name_second_player = input()

card_first_player = input()
card_second_player = input()

points_first_player = 0
points_second_player = 0

name_winner = None

while True:

    if int(card_first_player) > int(card_second_player):
        points_first_player += int(card_first_player) - int(card_second_player)

    elif int(card_first_player) < int(card_second_player):
        points_second_player += int(card_second_player) - int(card_first_player)

    elif int(card_first_player) == int(card_second_player):

        print("Number wars!")

        card_first_player = input()
        card_second_player = input()

        if int(card_first_player) > int(card_second_player):
            name_winner = name_first_player
            print(f"{name_winner} is winner with {points_first_player} points")

        elif int(card_first_player) < int(card_second_player):
            name_winner = name_second_player
            print(f"{name_winner} is winner with {points_second_player} points")

        break

    card_first_player = input()

    if card_first_player == "End of game":
        print(f"{name_first_player} has {points_first_player} points")
        print(f"{name_second_player} has {points_second_player} points")
        break

    card_second_player = input()
