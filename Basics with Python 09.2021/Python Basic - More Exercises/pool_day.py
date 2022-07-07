import math

number_of_people = int(input())
entrance_tax = float(input())
price_beds = float(input())
price_umbrellas = float(input())

number_umbrellas = math.ceil(number_of_people / 2)

number_beds = math.ceil(number_of_people - ((25 / 100) * number_of_people))

sum_people = (number_of_people * entrance_tax)
sum_beds = (number_beds * price_beds)
sum_umbrellas = (number_umbrellas * price_umbrellas)

total_sum = sum_people + sum_beds + sum_umbrellas

print(f"{total_sum:.2f} lv.")
