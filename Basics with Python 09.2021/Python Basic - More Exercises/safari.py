budget = float(input())
needed_fuel_litres = float(input())
day = input()

price_litre_fuel = 2.10
price_tour_guide = 100

total_sum = price_tour_guide + (needed_fuel_litres * price_litre_fuel)

if day == "Saturday":
    total_sum = total_sum - ((10 / 100) * total_sum)

elif day == "Sunday":
    total_sum = total_sum - ((20 / 100) * total_sum)

diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Safari time! Money left: {diff:.2f} lv. ")

else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
