import math

price_of_one_tennis_rocket = float(input())
number_of_tennis_rockets = int(input())
number_pair_of_sneakers = int(input())

price_of_one_pair_of_sneakers = (1 / 6) * price_of_one_tennis_rocket

sum_r = number_of_tennis_rockets * price_of_one_tennis_rocket
sum_s = number_pair_of_sneakers * price_of_one_pair_of_sneakers
sum_r_plus_s = sum_r + sum_s

price_others = (20 / 100) * sum_r_plus_s

total_sum = sum_r + sum_s + price_others

aaa = math.floor((1 / 8) * total_sum)
bbb = math.ceil((7 / 8) * total_sum)

print(f"Price to be paid by Djokovic {aaa}")
print(f"Price to be paid by sponsors {bbb}")
