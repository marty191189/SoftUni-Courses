number_of_days = int(input())
number_of_hours = int(input())
cost_for_all_period = 0
cost_for_the_day = 0

for day in range(1, number_of_days + 1):
    cost_for_the_day = 0
    for hour in range(1, number_of_hours + 1):
        if day % 2 == 0:
            if hour % 2 != 0:
                cost_for_all_period += 2.50
                cost_for_the_day += 2.50
            else:
                cost_for_all_period += 1
                cost_for_the_day += 1

        else:
            if hour % 2 == 0:
                cost_for_all_period += 1.25
                cost_for_the_day += 1.25
            else:
                cost_for_all_period += 1
                cost_for_the_day += 1

    print(f"Day: {day} - {cost_for_the_day:.2f} leva")

print(f"Total: {cost_for_all_period:.2f} leva")
