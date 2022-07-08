food = float(input())
hay = float(input())
cover = float(input())
pig_weight = float(input())

food_in_grams = food * 1000
hay_in_grams = hay * 1000
cover_in_grams = cover * 1000
pig_weight_in_grams = pig_weight * 1000

something_is_over = False

for day in range(1, 30 + 1):
    food_in_grams -= 300

    if day % 2 == 0:
        hay_in_grams = (hay_in_grams - ((5 / 100) * food_in_grams))

    if day % 3 == 0:
        cover_in_grams -= (1 / 3) * pig_weight_in_grams

    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        something_is_over = True
        break

if something_is_over:
    print("Merry must go to the pet store!")

else:
    print(f"Everything is fine! Puppy is happy! Food: {(food_in_grams/1000):.2f}, Hay: {(hay_in_grams/1000):.2f}, "
          f"Cover: {(cover_in_grams/1000):.2f}.")
