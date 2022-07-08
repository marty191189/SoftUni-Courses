days = int(input())
profit_per_day = int(input())
expected_profit = float(input())

total_profit = 0

for day in range(1, days + 1):
    total_profit += profit_per_day

    if day % 3 == 0 and day % 5 == 0:
        total_profit += (50 / 100) * profit_per_day
        total_profit -= (30 / 100) * total_profit

    elif day % 3 == 0:
        total_profit += (50 / 100) * profit_per_day

    elif day % 5 == 0:
        total_profit -= (30 / 100) * total_profit

if total_profit >= expected_profit:
    print(f"Ahoy! {total_profit:.2f} plunder gained.")

else:
    diff = (total_profit * 100) / expected_profit
    print(f"Collected only {diff:.2f}% of the plunder.")
