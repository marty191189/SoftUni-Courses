type_of_drink = input()
sugar_preference = input()
number_of_drinks = int(input())

price_drink = 0

if type_of_drink == "Espresso":

    if sugar_preference == "Without":
        price_drink = 0.90 * number_of_drinks
        price_drink = price_drink - ((35 / 100) * price_drink)

    elif sugar_preference == "Normal":
        price_drink = 1 * number_of_drinks

    elif sugar_preference == "Extra":
        price_drink = 1.20 * number_of_drinks

    if number_of_drinks >= 5:
        price_drink = price_drink - ((25 / 100) * price_drink)

elif type_of_drink == "Cappuccino":

    if sugar_preference == "Without":
        price_drink = 1 * number_of_drinks
        price_drink = price_drink - ((35 / 100) * price_drink)

    elif sugar_preference == "Normal":
        price_drink = 1.20 * number_of_drinks

    elif sugar_preference == "Extra":
        price_drink = 1.60 * number_of_drinks

elif type_of_drink == "Tea":

    if sugar_preference == "Without":
        price_drink = 0.50 * number_of_drinks
        price_drink = price_drink - ((35 / 100) * price_drink)

    elif sugar_preference == "Normal":
        price_drink = 0.60 * number_of_drinks

    elif sugar_preference == "Extra":
        price_drink = 0.70 * number_of_drinks

if price_drink > 15:
    price_drink = price_drink - ((20 / 100) * price_drink)

print(f"You bought {number_of_drinks} cups of {type_of_drink} for {price_drink:.2f} lv.")
