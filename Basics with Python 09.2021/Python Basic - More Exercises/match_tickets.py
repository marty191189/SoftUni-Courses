budget = float(input())
category_ticket = input()
number_of_people = int(input())

new_budget = 0
total_sum = 0

if 1 <= number_of_people <= 4:
    new_budget = budget - (75 / 100) * budget

elif 5 <= number_of_people <= 9:
    new_budget = budget - (60 / 100) * budget

elif 10 <= number_of_people <= 24:
    new_budget = budget - (50 / 100) * budget

elif 25 <= number_of_people <= 49:
    new_budget = budget - (40 / 100) * budget

elif 50 <= number_of_people:
    new_budget = budget - (25 / 100) * budget

if category_ticket == "Normal":
    normal_ticket = 249.99
    total_sum = number_of_people * normal_ticket

    diff = abs(new_budget - total_sum)

    if new_budget >= total_sum:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff:.2f} leva.")

elif category_ticket == "VIP":
    vip_ticket = 499.99
    total_sum = number_of_people * vip_ticket

    diff = abs(new_budget - total_sum)

    if new_budget >= total_sum:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff:.2f} leva.")
