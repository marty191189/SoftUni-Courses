pirate_ship = input().split(">")
pirate_ship = list(map(int, pirate_ship))

warship = input().split(">")
warship = list(map(int, warship))

maximum_health = int(input())

pirate_ship_has_sunk = False
warship_has_sunk = False
nobody_wins = True

command = input()

while not command == "Retire":

    data = command.split()

    if data[0] == "Fire":
        index = int(data[1])
        damage = int(data[2])

        if index in range(0, len(warship)):

            warship[index] -= damage

            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                warship_has_sunk = True
                nobody_wins = False
                break

    elif data[0] == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])

        if start_index in range(0, len(pirate_ship)) and end_index in range(0, len(pirate_ship)):

            for index in range(0, len(pirate_ship)):
                if index in range(start_index, end_index + 1):
                    pirate_ship[index] -= damage

            for el in pirate_ship:
                if el <= 0:
                    pirate_ship_has_sunk = True
                    break

            if pirate_ship_has_sunk:
                print("You lost! The pirate ship has sunken.")
                nobody_wins = False
                break

    elif data[0] == "Repair":
        index = int(data[1])
        health = int(data[2])

        if index in range(0, len(pirate_ship)):

            if pirate_ship[index] + health <= maximum_health:
                pirate_ship[index] += health

            elif pirate_ship[index] + health > maximum_health:
                diff = maximum_health - pirate_ship[index]
                pirate_ship[index] += diff

    elif data[0] == "Status":

        counter_sections = 0

        minimum_health = ((20 / 100) * maximum_health)

        for el in pirate_ship:
            if el < minimum_health:
                counter_sections += 1

        print(f"{counter_sections} sections need repair.")

    command = input()

if nobody_wins:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")


# втори начин
#
# pirate_ship = [int(num) for num in input().split(">")]
# warship = [int(num) for num in input().split(">")]
#
# max_health_capacity = int(input())
#
# command = input()
# is_sunk = False
#
# while not command == "Retire":
#     data = command.split()
#     if data[0] == "Fire":
#         index = int(data[1])
#         damage = int(data[2])
#         if 0 <= index < len(warship):
#             warship[index] -= damage
#             if warship[index] <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 is_sunk = True
#                 break
#     elif data[0] == "Defend":
#         start_index = int(data[1])
#         end_index = int(data[2])
#         damage = int(data[3])
#         if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
#             for index in range(start_index, end_index + 1):
#                 pirate_ship[index] -= damage
#                 if pirate_ship[index] <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     is_sunk = True
#                     break
#
#     elif data[0] == "Repair":
#         index = int(data[1])
#         health = int(data[2])
#         if 0 <= index < len(pirate_ship):
#             if pirate_ship[index] + health > max_health_capacity:
#                 pirate_ship[index] = max_health_capacity
#             else:
#                 pirate_ship[index] += health
#     elif data[0] == "Status":
#         threshold = max_health_capacity * 0.2
#         counter = 0
#         for num in pirate_ship:
#             if num < threshold:
#                 counter += 1
#         print(f"{counter} sections need repair.")
#     command = input()
#
# if not is_sunk:
#     print(f"Pirate ship status: {sum(pirate_ship)}")
#     print(f"Warship status: {sum(warship)}")
