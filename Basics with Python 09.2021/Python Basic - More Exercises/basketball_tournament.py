name_of_tournament = input()
number_of_games = int(input())

counter_won_games = 0
counter_lost_games = 0
all_games = 0

while True:

    for game in range(1, number_of_games + 1):

        points_desi_team = int(input())
        points_other_team = int(input())

        if points_desi_team > points_other_team:
            counter_won_games += 1
            all_games += 1
            diff = points_desi_team - points_other_team
            print(f"Game {game} of tournament {name_of_tournament}: win with {diff} points.")

        elif points_desi_team < points_other_team:
            counter_lost_games += 1
            all_games += 1
            diff = points_other_team - points_desi_team
            print(f"Game {game} of tournament {name_of_tournament}: lost with {diff} points.")

    name_of_tournament = input()

    if name_of_tournament == "End of tournaments":
        break

    number_of_games = int(input())

perc_won_games = (counter_won_games / all_games) * 100
perc_lost_games = (counter_lost_games / all_games) * 100

print(f"{perc_won_games:.2f}% matches win")
print(f"{perc_lost_games:.2f}% matches lost")
