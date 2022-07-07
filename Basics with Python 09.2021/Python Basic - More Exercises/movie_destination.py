budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

total_sum = 0

if season == "Winter":

    if destination == "Dubai":
        total_sum = number_of_days * 45000
        total_sum = total_sum - ((30 / 100) * total_sum)

    elif destination == "Sofia":
        total_sum = number_of_days * 17000
        total_sum = total_sum + ((25 / 100) * total_sum)

    elif destination == "London":
        total_sum = number_of_days * 24000

elif season == "Summer":

    if destination == "Dubai":
        total_sum = number_of_days * 40000
        total_sum = total_sum - ((30 / 100) * total_sum)

    elif destination == "Sofia":
        total_sum = number_of_days * 12500
        total_sum = total_sum + ((25 / 100) * total_sum)

    elif destination == "London":
        total_sum = number_of_days * 20250

diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")

else:
    print(f"The director needs {diff:.2f} leva more!")
