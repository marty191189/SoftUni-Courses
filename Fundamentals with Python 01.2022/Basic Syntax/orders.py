number_of_orders = int(input())
total_price = 0

for i in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    current_price = price_per_capsule * capsules_count * days

    print(f"The price for the coffee is: ${current_price:.2f}")

    total_price += current_price

print(f"Total: ${total_price:.2f}")
