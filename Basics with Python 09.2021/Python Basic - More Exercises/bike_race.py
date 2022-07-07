number_junior_bikers = int(input())
number_senior_bikers = int(input())
type_of_terrain = input()

total_sum = 0

number_all_bikers = number_junior_bikers + number_senior_bikers

sum1 = 0
sum2 = 0

donated_sum = 0

if type_of_terrain == "trail":
    sum1 = number_junior_bikers * 5.50
    sum2 = number_senior_bikers * 7

elif type_of_terrain == "cross-country":
    if 50 <= number_all_bikers:
        discount1 = 8 - ((25 / 100) * 8)
        discount2 = 9.50 - ((25 / 100) * 9.50)
        sum1 = number_junior_bikers * discount1
        sum2 = number_senior_bikers * discount2

    else:
        sum1 = number_junior_bikers * 8
        sum2 = number_senior_bikers * 9.50

elif type_of_terrain == "downhill":
    sum1 = number_junior_bikers * 12.25
    sum2 = number_senior_bikers * 13.75

elif type_of_terrain == "road":
    sum1 = number_junior_bikers * 20
    sum2 = number_senior_bikers * 21.50

total_sum = sum1 + sum2
expenses = ((5 / 100) * total_sum)
donated_sum = total_sum - ((5 / 100) * total_sum)

print(f"{donated_sum:.2f}")
