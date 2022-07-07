budget = float(input())
number_of_series = int(input())

total_sum = 0

for number in range(1, number_of_series + 1):

    name_of_series = input()

    price_of_series = float(input())

    if name_of_series == "Thrones":
        price_of_series = price_of_series - ((50 / 100) * price_of_series)

    elif name_of_series == "Lucifer":
        price_of_series = price_of_series - ((40 / 100) * price_of_series)

    elif name_of_series == "Protector":
        price_of_series = price_of_series - ((30 / 100) * price_of_series)

    elif name_of_series == "TotalDrama":
        price_of_series = price_of_series - ((20 / 100) * price_of_series)

    elif name_of_series == "Area":
        price_of_series = price_of_series - ((10 / 100) * price_of_series)

    total_sum += price_of_series

diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"You bought all the series and left with {diff:.2f} lv.")

else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
