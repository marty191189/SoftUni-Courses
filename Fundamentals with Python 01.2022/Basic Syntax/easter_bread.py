budget = float(input())
price_for_1_kg_flour = float(input())

counter_eggs = 0
number_of_bread = 0
new_bread = False

price_for_1_pack_of_eggs = ((75 / 100) * price_for_1_kg_flour)
price_for_1l_milk = price_for_1_kg_flour + ((25 / 100) * price_for_1_kg_flour)
price_for_250ml_milk = price_for_1l_milk / 4

price_for_1_bread = (price_for_1_pack_of_eggs + price_for_1_kg_flour + price_for_250ml_milk)

while budget > price_for_1_bread:

    budget -= price_for_1_bread

    if budget > 0:
        number_of_bread += 1
        new_bread = True

    if new_bread:
        counter_eggs += 3

    if number_of_bread % 3 == 0:
        counter_eggs -= (number_of_bread - 2)

print(f"You made {number_of_bread} loaves of Easter bread! Now you have {counter_eggs} eggs and {budget:.2f}BGN left.")
