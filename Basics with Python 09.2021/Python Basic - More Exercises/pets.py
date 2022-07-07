import math

days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_grams = float(input())

turtle_food_kg = turtle_food_grams / 1000

total_needed_food = (days * dog_food_kg) + (days * cat_food_kg) + (days * turtle_food_kg)

diff = abs(total_needed_food - food_kg)

if food_kg >= total_needed_food:
    print(f"{math.floor(diff)} kilos of food left.")

else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")

# import math
#
# days = int(input())
# food_kg = int(input())
# dog_food_kg = float(input())
# cat_food_kg = float(input())
# turtle_food_grams = float(input())
#
# turtle_food_kg = turtle_food_grams / 1000
#
# total_needed_food = (days * dog_food_kg) + (days * cat_food_kg) + (days * turtle_food_kg)
#
# if food_kg >= total_needed_food:
#     kg_saved = food_kg - total_needed_food
#     print(f"{math.floor(kg_saved)} kilos of food left.")
#
# else:
#     kg_needed = total_needed_food - food_kg
#     print(f"{math.ceil(kg_needed)} more kilos of food are needed.")
