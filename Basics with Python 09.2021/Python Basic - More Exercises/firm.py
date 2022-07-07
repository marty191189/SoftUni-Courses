import math

needed_hours = int(input())
days = int(input())
workers_overtime = int(input())

days_minus_10_perc = days - ((10 / 100) * days)

actual_working_hours = days_minus_10_perc * 8

working_hours_overtime = workers_overtime * (2 * days)

total_hours = actual_working_hours + working_hours_overtime

diff = abs(needed_hours - math.floor(total_hours))

if math.floor(total_hours) >= needed_hours:
    print(f"Yes!{diff} hours left.")

else:
    print(f"Not enough time!{diff} hours needed.")
