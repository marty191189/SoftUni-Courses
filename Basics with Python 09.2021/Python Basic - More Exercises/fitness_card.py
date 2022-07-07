budget = float(input())
sex = input()
age = int(input())
sport = input()

total_sum = 0

if sex == "m":

    if sport == "Gym":
        total_sum += 42

    elif sport == "Boxing":
        total_sum += 41

    elif sport == "Yoga":
        total_sum += 45

    elif sport == "Zumba":
        total_sum += 34

    elif sport == "Dances":
        total_sum += 51

    elif sport == "Pilates":
        total_sum += 39

elif sex == "f":

    if sport == "Gym":
        total_sum += 35

    elif sport == "Boxing":
        total_sum += 37

    elif sport == "Yoga":
        total_sum += 42

    elif sport == "Zumba":
        total_sum += 31

    elif sport == "Dances":
        total_sum += 53

    elif sport == "Pilates":
        total_sum += 37

if age <= 19:
    total_sum = total_sum - ((20 / 100) * total_sum)

money = abs(total_sum - budget)

if total_sum <= budget:
    print(f"You purchased a 1 month pass for {sport}.")

else:
    print(f"You don't have enough money! You need ${money:.2f} more.")
