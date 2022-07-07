import math

number_tournaments_played = int(input())
starting_points = int(input())

average_points = 0
final_points = 0
percent_won_tournaments = 0
all_tournaments = 0
won_tournaments = 0

counter_w = 0
counter_f = 0
counter_sf = 0

for tournament in range(1, number_tournaments_played + 1):
    stage_of_tournament = input()

    if stage_of_tournament == "W":
        final_points += 2000
        all_tournaments += 1
        won_tournaments += 1
        counter_w += 1

    elif stage_of_tournament == "F":
        final_points += 1200
        all_tournaments += 1
        counter_f += 1

    elif stage_of_tournament == "SF":
        final_points += 720
        all_tournaments += 1
        counter_sf += 1

final_points += starting_points

sum_counter = (counter_w * 2000) + (counter_f * 1200) + (counter_sf * 720)

average_points = sum_counter / all_tournaments

final_percent = (won_tournaments / all_tournaments) * 100

print(f"Final points: {final_points}")

print(f"Average points: {math.floor(average_points)}")

print(f"{final_percent:.2f}%")
