number_of_commands = int(input())

parking_dict = {}

for number in range(1, number_of_commands + 1):
    data = input().split(" ")

    action = data[0]

    if action == "register":

        person_name = data[1]
        car_number = data[2]

        if person_name not in parking_dict:
            parking_dict[person_name] = car_number
            print(f"{person_name} registered {car_number} successfully")

        else:
            print(f"ERROR: already registered with plate number {car_number}")

    elif action == "unregister":

        person_name = data[1]

        if person_name not in parking_dict:
            print(f"ERROR: user {person_name} not found")

        else:
            del parking_dict[person_name]
            print(f"{person_name} unregistered successfully")

for key, value in parking_dict.items():
    print(f"{key} => {value}")
