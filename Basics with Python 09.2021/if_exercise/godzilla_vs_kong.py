budget = float(input())
number_of_statists = int(input())
one_clothing_price = float(input())
decor = budget * 0.1
clothing_price = number_of_statists * one_clothing_price

if number_of_statists > 150:
    clothing_price *= 0.9

needed_money = decor + clothing_price
diff = abs(needed_money - budget)
if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
