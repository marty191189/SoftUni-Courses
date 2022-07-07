price_of_bag_above_20_kg = float(input())
kg_bag = float(input())
days_till_vacation = int(input())
number_of_bags = int(input())

bag_tax = 0
total_sum = 0

if kg_bag < 10:
    bag_tax = (20 / 100)
    total_sum = price_of_bag_above_20_kg * bag_tax

elif 10 <= kg_bag <= 20:
    bag_tax = (50 / 100)
    total_sum = price_of_bag_above_20_kg * bag_tax

elif kg_bag > 20:
    total_sum = price_of_bag_above_20_kg

if days_till_vacation < 7:
    total_sum = total_sum + ((40 / 100) * total_sum)

elif 7 <= days_till_vacation <= 30:
    total_sum = total_sum + ((15 / 100) * total_sum)

elif days_till_vacation > 30:
    total_sum = total_sum + ((10 / 100) * total_sum)

total_sum = total_sum * number_of_bags

print(f"The total price of bags is: {total_sum:.2f} lv.")
