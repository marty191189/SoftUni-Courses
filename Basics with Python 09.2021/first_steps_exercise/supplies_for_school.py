box_pens = int(input())
box_markers = int(input())
liters_of_chemical = float(input())
discount_percent = int(input())

price_per_pen = 5.80
price_per_marker = 7.20
price_per_litre = 1.20

total_sum = (box_pens * price_per_pen) + (box_markers * price_per_marker) + (liters_of_chemical * price_per_litre)

needed_money = total_sum - ((discount_percent / 100) * total_sum)

print(needed_money)
