fuel_name = input()
litres_of_fuel = float(input())
owning_discount_card = input()

fuel_name = fuel_name.lower()

final_price = 0
discount_price = 0
price1 = 0
price2 = 0

if fuel_name == "gasoline":
    if owning_discount_card == "Yes":
        discount_price = 2.22 - 0.18

    if litres_of_fuel < 20:
        price2 = litres_of_fuel * discount_price

    if 20 <= litres_of_fuel <= 25:
        price1 = litres_of_fuel * discount_price
        price2 = (price1 - ((8 / 100) * price1))

    elif litres_of_fuel > 25:
        price1 = litres_of_fuel * discount_price
        price2 = (price1 - ((10 / 100) * price1))

    if owning_discount_card == "No":

        if litres_of_fuel < 20:
            price2 = litres_of_fuel * 2.22

        if 20 <= litres_of_fuel <= 25:
            price1 = litres_of_fuel * 2.22
            price2 = (price1 - ((8 / 100) * price1))

        elif litres_of_fuel > 25:
            price1 = litres_of_fuel * 2.22
            price2 = (price1 - ((10 / 100) * price1))

if fuel_name == "diesel":
    if owning_discount_card == "Yes":
        discount_price = 2.33 - 0.12

    if litres_of_fuel < 20:
        price2 = litres_of_fuel * discount_price

    if 20 <= litres_of_fuel <= 25:
        price1 = litres_of_fuel * discount_price
        price2 = (price1 - ((8 / 100) * price1))

    elif litres_of_fuel > 25:
        price1 = litres_of_fuel * discount_price
        price2 = (price1 - ((10 / 100) * price1))

    if owning_discount_card == "No":

        if litres_of_fuel < 20:
            price2 = litres_of_fuel * 2.33

        if 20 <= litres_of_fuel <= 25:
            price1 = litres_of_fuel * 2.33
            price2 = (price1 - ((8 / 100) * price1))

        elif litres_of_fuel > 25:
            price1 = litres_of_fuel * 2.33
            price2 = (price1 - ((10 / 100) * price1))

if fuel_name == "gas":
    if owning_discount_card == "Yes":
        discount_price = 0.93 - 0.08

    if litres_of_fuel < 20:
        price2 = litres_of_fuel * discount_price

    if 20 <= litres_of_fuel <= 25:
        price1 = litres_of_fuel * discount_price
        price2 = (price1 - ((8 / 100) * price1))

    elif litres_of_fuel > 25:
        price1 = litres_of_fuel * discount_price
        price2 = (price1 - ((10 / 100) * price1))

    if owning_discount_card == "No":

        if litres_of_fuel < 20:
            price2 = litres_of_fuel * 0.93

        if 20 <= litres_of_fuel <= 25:
            price1 = litres_of_fuel * 0.93
            price2 = (price1 - ((8 / 100) * price1))

        elif litres_of_fuel > 25:
            price1 = litres_of_fuel * 0.93
            price2 = (price1 - ((10 / 100) * price1))

final_price = price2
print(f"{final_price:.2f} lv.")
