budget = float(input())
season = input()

final_price = 0
place = None
location = None

if budget <= 1000:
    place = "Camp"

    if season == "Summer":
        location = "Alaska"

        final_price = ((65 / 100) * budget)

    elif season == "Winter":
        location = "Morocco"

        final_price = ((45 / 100) * budget)

elif 1000 < budget <= 3000:
    place = "Hut"

    if season == "Summer":
        location = "Alaska"

        final_price = ((80 / 100) * budget)

    elif season == "Winter":
        location = "Morocco"

        final_price = ((60 / 100) * budget)

elif 3000 < budget:
    place = "Hotel"

    if season == "Summer":
        location = "Alaska"

        final_price = ((90 / 100) * budget)

    elif season == "Winter":
        location = "Morocco"

        final_price = ((90 / 100) * budget)

print(f"{location} - {place} - {final_price:.2f}")
