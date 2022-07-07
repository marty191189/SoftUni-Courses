number_of_km = int(input())
day_or_night = input()

price_taxi = 0
price_bus = 0
price_train = 0
final_price = 0

if day_or_night == "day":
    if number_of_km < 20:
        price_taxi = (number_of_km * 0.79) + 0.70
        final_price = price_taxi

    if 20 <= number_of_km < 100:
        price_bus = number_of_km * 0.09
        final_price = price_bus

    if number_of_km >= 100:
        price_train = number_of_km * 0.06
        final_price = price_train

if day_or_night == "night":
    if number_of_km < 20:
        price_taxi = (number_of_km * 0.90) + 0.70
        final_price = price_taxi

    if 20 <= number_of_km < 100:
        price_bus = number_of_km * 0.09
        final_price = price_bus

    if number_of_km >= 100:
        price_train = number_of_km * 0.06
        final_price = price_train

print(f"{final_price:.2f}")
