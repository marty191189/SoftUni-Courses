budget = float(input())
costs = 0
counter_of_product = 0
budget_condition = True
needed_money = 0

while True:
    name_of_product = input()

    if name_of_product == "Stop":
        break

    price_of_product = float(input())

    counter_of_product += 1

    if counter_of_product % 3 == 0:
        price_of_product = price_of_product / 2

    if price_of_product > budget:
        budget_condition = False
        needed_money = price_of_product - budget
        counter_of_product -= 1
        break

    costs += price_of_product
    budget -= price_of_product

if budget_condition:
    print(f"You bought {counter_of_product} products for {costs:.2f} leva.")

else:
    print(f"You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")
