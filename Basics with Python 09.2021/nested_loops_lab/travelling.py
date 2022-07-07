budget = 0
while True:
    destination = input()
    if destination == "End":
        break
    price_vacation = float(input())
    budget = 0
    while price_vacation > budget:
        currently_saved_money = float(input())
        budget += currently_saved_money
        if budget >= price_vacation:
            print(f"Going to {destination}!")
            break
