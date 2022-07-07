budget = int(input())
season = input()
number_of_fishermen = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000

    if number_of_fishermen <= 6:
        boat_rent = boat_rent - ((10 / 100) * boat_rent)

    elif 7 <= number_of_fishermen <= 11:
        boat_rent = boat_rent - ((15 / 100) * boat_rent)

    elif 12 <= number_of_fishermen:
        boat_rent = boat_rent - ((25 / 100) * boat_rent)

elif season == "Summer":
    boat_rent = 4200

    if number_of_fishermen <= 6:
        boat_rent = boat_rent - ((10 / 100) * boat_rent)

    elif 7 <= number_of_fishermen <= 11:
        boat_rent = boat_rent - ((15 / 100) * boat_rent)

    elif 12 <= number_of_fishermen:
        boat_rent = boat_rent - ((25 / 100) * boat_rent)

elif season == "Autumn":
    boat_rent = 4200

    if number_of_fishermen <= 6:
        boat_rent = boat_rent - ((10 / 100) * boat_rent)

    elif 7 <= number_of_fishermen <= 11:
        boat_rent = boat_rent - ((15 / 100) * boat_rent)

    elif 12 <= number_of_fishermen:
        boat_rent = boat_rent - ((25 / 100) * boat_rent)

elif season == "Winter":
    boat_rent = 2600

    if number_of_fishermen <= 6:
        boat_rent = boat_rent - ((10 / 100) * boat_rent)

    elif 7 <= number_of_fishermen <= 11:
        boat_rent = boat_rent - ((15 / 100) * boat_rent)

    elif 12 <= number_of_fishermen:
        boat_rent = boat_rent - ((25 / 100) * boat_rent)

if (number_of_fishermen % 2 == 0) and season != "Autumn":
    boat_rent = boat_rent - ((5 / 100) * boat_rent)

diff = abs(boat_rent - budget)

if budget >= boat_rent:
    print(f"Yes! You have {diff:.2f} leva left.")

else:
    print(f"Not enough money! You need {diff:.2f} leva.")
