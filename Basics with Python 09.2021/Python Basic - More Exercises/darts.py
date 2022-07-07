name_of_player = input()

starting_points = 301
counter_successful_shots = 0
counter_unsuccessful_shots = 0
current_points = 0

zone = input()
points = int(input())

while True:

    if zone == "Retire":
        print(f"{name_of_player} retired after {counter_unsuccessful_shots} unsuccessful shots.")
        break

    if zone == "Single":
        current_points = points

        if starting_points >= current_points:
            starting_points -= current_points
            counter_successful_shots += 1

        elif starting_points < current_points:
            counter_unsuccessful_shots += 1

    elif zone == "Double":
        current_points = points * 2

        if starting_points >= current_points:
            starting_points -= current_points
            counter_successful_shots += 1

        elif starting_points < current_points:
            counter_unsuccessful_shots += 1

    elif zone == "Triple":
        current_points = points * 3

        if starting_points >= current_points:
            starting_points -= current_points
            counter_successful_shots += 1

        elif starting_points < current_points:
            counter_unsuccessful_shots += 1

    if starting_points <= 0:
        print(f"{name_of_player} won the leg with {counter_successful_shots} shots.")
        break

    zone = input()

    if zone == "Retire":
        print(f"{name_of_player} retired after {counter_unsuccessful_shots} unsuccessful shots.")
        break

    points = int(input())
