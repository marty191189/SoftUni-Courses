name_of_team = input()
number_of_played_games = int(input())

counter_w = 0
counter_d = 0
counter_l = 0
counter_all_games = 0
points = 0

if number_of_played_games != 0:

    for number in range(1, number_of_played_games + 1):

        result_of_game = input()

        if result_of_game == "W":
            counter_w += 1
            counter_all_games += 1
            points += 3

        elif result_of_game == "D":
            counter_d += 1
            counter_all_games += 1
            points += 1

        elif result_of_game == "L":
            counter_l += 1
            counter_all_games += 1
            points += 0

    win_rate = (counter_w / counter_all_games) * 100

    print(f"{name_of_team} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {counter_w}")
    print(f"## D: {counter_d}")
    print(f"## L: {counter_l}")
    print(f"Win rate: {win_rate:.2f}%")

else:
    print(f"{name_of_team} hasn't played any games during this season.")
