bought_food_in_kg = int(input())

bought_food_in_gr = bought_food_in_kg * 1000

total_eaten_food = 0

eaten_food = input()

while True:

    if eaten_food == "Adopted":
        break

    total_eaten_food += int(eaten_food)

    eaten_food = input()

diff = abs(bought_food_in_gr - total_eaten_food)

if total_eaten_food <= bought_food_in_gr:
    print(f"Food is enough! Leftovers: {diff} grams.")

else:
    print(f"Food is not enough. You need {diff} grams more.")
