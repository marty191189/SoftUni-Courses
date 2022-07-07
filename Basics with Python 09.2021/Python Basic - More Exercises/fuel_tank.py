type_of_fuel = input()
available_fuel = float(input())

fuel_name = type_of_fuel.lower()

if fuel_name == "diesel" or fuel_name == "gasoline" or fuel_name == "gas":
    if available_fuel >= 25:
        print(f"You have enough {fuel_name}.")
    else:
        print(f"Fill your tank with {fuel_name}!")
else:
    print("Invalid fuel!")
