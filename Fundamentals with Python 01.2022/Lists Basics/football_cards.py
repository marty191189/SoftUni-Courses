info = input().split(" ")
team_a_players = 11
team_b_players = 11
game_was_terminated = False

players_out = []

for card in info:
    if card not in players_out:
        players_out.append(card)

        if "A" in card:
            team_a_players -= 1

        if "B" in card:
            team_b_players -= 1

        if team_a_players < 7 or team_b_players < 7:
            game_was_terminated = True
            break

print(f"Team A - {team_a_players}; Team B - {team_b_players}")

if game_was_terminated:
    print("Game was terminated")
