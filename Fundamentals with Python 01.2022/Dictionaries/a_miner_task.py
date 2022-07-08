command = input()

resources_dict = {}

resource = ""
quantity = ""

counter = 0

while not command == "stop":
    counter += 1

    if counter % 2 != 0:
        resource = command
        if resource not in resources_dict:
            resources_dict[resource] = 0

    elif counter % 2 == 0:
        quantity = int(command)
        resources_dict[resource] += quantity

    command = input()

for key, value in resources_dict.items():
    print(f"{key} -> {value}")
