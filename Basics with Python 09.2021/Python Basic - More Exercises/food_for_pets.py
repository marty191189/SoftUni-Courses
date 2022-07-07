number_of_days = int(input())
total_amount_of_food = float(input())

all_eaten_biscuits = 0
all_dog_eaten_food = 0
all_cat_eaten_food = 0
all_eaten_food = 0

for day in range(1, number_of_days + 1):

    dog_food = int(input())
    cat_food = int(input())

    total_food_current_day = dog_food + cat_food

    if day % 3 == 0:

        biscuits = (10 / 100) * total_food_current_day
        all_eaten_biscuits += biscuits

    all_dog_eaten_food += dog_food
    all_cat_eaten_food += cat_food

all_eaten_food = all_dog_eaten_food + all_cat_eaten_food

perc_all_eaten_food = (all_eaten_food / total_amount_of_food) * 100
perc_dog_eaten_food = (all_dog_eaten_food / all_eaten_food) * 100
perc_cat_eaten_food = (all_cat_eaten_food / all_eaten_food) * 100

# print(f"Total eaten biscuits: {round(all_eaten_biscuits)}gr.")
print(f"Total eaten biscuits: {int(all_eaten_biscuits)}gr.")
print(f"{perc_all_eaten_food:.2f}% of the food has been eaten.")
print(f"{perc_dog_eaten_food:.2f}% eaten from the dog.")
print(f"{perc_cat_eaten_food:.2f}% eaten from the cat.")
