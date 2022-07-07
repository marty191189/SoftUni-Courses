budget = float(input())
season = input()

if season == "summer":
    if budget <= 100:
        budget = ((30 / 100) * budget)
        print(f"Somewhere in Bulgaria")
        print(f"Camp - {budget:.2f}")

    elif budget <= 1000:
        budget = ((40 / 100) * budget)
        print(f"Somewhere in Balkans")
        print(f"Camp - {budget:.2f}")

    elif budget > 1000:
        budget = ((90 / 100) * budget)
        print(f"Somewhere in Europe")
        print(f"Hotel - {budget:.2f}")

elif season == "winter":
    if budget <= 100:
        budget = ((70 / 100) * budget)
        print(f"Somewhere in Bulgaria")
        print(f"Hotel - {budget:.2f}")

    elif budget <= 1000:
        budget = ((80 / 100) * budget)
        print(f"Somewhere in Balkans")
        print(f"Hotel - {budget:.2f}")

    elif budget > 1000:
        budget = ((90 / 100) * budget)
        print(f"Somewhere in Europe")
        print(f"Hotel - {budget:.2f}")
