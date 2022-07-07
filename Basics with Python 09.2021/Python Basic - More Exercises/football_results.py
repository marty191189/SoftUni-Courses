result_from_first_match = input()
result_from_second_match = input()
result_from_third_match = input()

counter_won_matches = 0
counter_lost_matches = 0
counter_drawn_matches = 0

my_team_goals = int(result_from_first_match[0])
other_team_goals = int(result_from_first_match[2])

if my_team_goals > other_team_goals:
    counter_won_matches += 1

elif my_team_goals < other_team_goals:
    counter_lost_matches += 1

elif my_team_goals == other_team_goals:
    counter_drawn_matches += 1

my_team_goals = int(result_from_second_match[0])
other_team_goals = int(result_from_second_match[2])

if my_team_goals > other_team_goals:
    counter_won_matches += 1

if my_team_goals < other_team_goals:
    counter_lost_matches += 1

if my_team_goals == other_team_goals:
    counter_drawn_matches += 1

my_team_goals = int(result_from_third_match[0])
other_team_goals = int(result_from_third_match[2])

if my_team_goals > other_team_goals:
    counter_won_matches += 1

if my_team_goals < other_team_goals:
    counter_lost_matches += 1

if my_team_goals == other_team_goals:
    counter_drawn_matches += 1

print(f"Team won {counter_won_matches} games.")
print(f"Team lost {counter_lost_matches} games.")
print(f"Drawn games: {counter_drawn_matches}")
