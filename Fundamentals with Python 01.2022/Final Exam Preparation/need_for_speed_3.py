number_of_lines = int(input())

car_dict = {}

for number in range(1, number_of_lines + 1):

    info = input().split("|")

    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])

    if car not in car_dict:
        car_dict[car] = []
        car_dict[car].append(mileage)
        car_dict[car].append(fuel)

    else:
        car_dict[car][0] += mileage
        car_dict[car][1] += fuel

command = input()

while not command == "Stop":

    data = command.split(" : ")

    if data[0] == "Drive":
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])

        if fuel > car_dict[car][1]:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car][0] += distance
            car_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if car_dict[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del car_dict[car]

    if data[0] == "Refuel":
        car = data[1]
        new_fuel = int(data[2])

        if (car_dict[car][1] + new_fuel) <= 75:
            car_dict[car][1] += new_fuel
            print(f"{car} refueled with {new_fuel} liters")

        else:
            diff = 75 - car_dict[car][1]
            car_dict[car][1] += diff
            print(f"{car} refueled with {diff} liters")

    if data[0] == "Revert":
        car = data[1]
        kilometers = int(data[2])

        car_dict[car][0] -= kilometers

        if car_dict[car][0] < 10000:
            car_dict[car][0] = 10000

        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for key, value in car_dict.items():
    print(f"{key} -> Mileage: {car_dict[key][0]} kms, Fuel in the tank: {car_dict[key][1]} lt.")
