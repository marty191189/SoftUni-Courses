starting_points = int(input())
sum_bonus_points = 0

if starting_points <= 100:
    sum_bonus_points += 5

elif starting_points > 1000:
    sum_bonus_points = (10 / 100) * starting_points

else:
    sum_bonus_points = (20 / 100) * starting_points

if starting_points % 2 == 0:
    sum_bonus_points += 1

elif starting_points % 10 == 5:
    sum_bonus_points += 2

print(sum_bonus_points)
print(starting_points + sum_bonus_points)
