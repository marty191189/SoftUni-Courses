import math

number_of_people = int(input())
days = int(input())

coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        number_of_people -= 2

    if day % 15 == 0:
        number_of_people += 5

    coins_for_food = number_of_people * 2
    coins += (50 - coins_for_food)

    if day % 3 == 0:
        coins -= (number_of_people * 3)

    if day % 5 == 0:
        coins += (number_of_people * 20)

        if day % 3 == 0:
            coins -= (number_of_people * 2)

split_coins = math.floor(coins / number_of_people)

print(f"{number_of_people} companions received {split_coins} coins each.")
