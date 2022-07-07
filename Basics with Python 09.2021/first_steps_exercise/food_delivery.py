number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegan_menu = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15

sum1 = (chicken_menu * number_chicken_menu) + (fish_menu * number_fish_menu) + (vegan_menu * number_vegan_menu)

dessert = (20 / 100) * sum1

delivery = 2.50

total_sum = sum1 + dessert + delivery

print(total_sum)
