number_of_cars = int(input())

cars_set = set()

for number in range(1, number_of_cars + 1):
    data = input().split(", ")
    command = data[0]
    car_number = data[1]

    if command == "IN":
        cars_set.add(car_number)

    elif command == "OUT":
        cars_set.remove(car_number)

if not cars_set:
    print("Parking Lot is Empty")
else:
    print("\n".join(cars_set))
