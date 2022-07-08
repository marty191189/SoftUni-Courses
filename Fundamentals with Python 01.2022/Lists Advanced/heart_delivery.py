houses_list = input().split("@")
houses_list = list(map(int, houses_list))

house_index = 0

command = input()

while not command == "Love!":

    data = command.split()

    new_index = int(data[1])

    house_index += new_index

    if house_index not in range(0, len(houses_list)):
        house_index = 0

    current_house = houses_list[house_index]

    if current_house == 0:
        print(f"Place {house_index} already had Valentine's day.")

    elif current_house > 0:

        current_house -= 2

        if current_house == 0:
            print(f"Place {house_index} has Valentine's day.")
            houses_list[house_index] = current_house

        elif current_house > 0:
            houses_list[house_index] = current_house

    command = input()

print(f"Cupid's last position was {house_index}.")

a = houses_list.count(0)

if a == len(houses_list):
    print("Mission was successful.")

else:
    counter_houses = 0

    for house in houses_list:
        if not house == 0:
            counter_houses += 1

    print(f"Cupid has failed {counter_houses} places.")


# втори начин
#
# def representation_data(data, last_position):
#     result = [x for x in data if x == 0]
#     print(f"Cupid's last position was {last_position}.")
#
#     if len(result) != len(data):
#         diff = len(data) - len(result)
#         print(f"Cupid has failed {diff} places.")
#     else:
#         print("Mission was successful.")
#
#
# def heart_delivery(data):
#     current_index_position = 0
#     cupid_last_position = 0
#
#     while True:
#         command = input().split(" ")
#
#         if command[0] == "Love!":
#             break
#
#         index = int(command[1]) + current_index_position
#
#         if index >= len(data):
#             index = 0
#
#         if -1 < index < len(data):
#             if data[index] > 0:
#                 data[index] -= 2
#                 if data[index] == 0:
#                     print(f"Place {index} has Valentine's day.")
#             else:
#                 print(f"Place {index} already had Valentine's day.")
#
#         cupid_last_position = index
#         current_index_position = index
#
#     representation_data(data, cupid_last_position)
#
#
# nums = list(map(int, input().split("@")))
# heart_delivery(nums)


# трети начин
#
# neighborhood = [int(num) for num in input().split("@")]
#
# command = input()
# position = 0
#
# while not command == "Love!":
#     length_jump = command.split()[1]
#     length_jump = int(length_jump)
#
#     position = position + length_jump
#
#     if position >= len(neighborhood):
#         position = 0
#
#     if neighborhood[position] == 0:
#         print(f"Place {position} already had "
#               f"Valentine's day.")
#     else:
#         neighborhood[position] -= 2
#         if neighborhood[position] == 0:
#             print(f"Place {position} has Valentine's day.")
#
#     command = input()
#
# print(f"Cupid's last position was {position}.")
#
# counter = 0
# for num in neighborhood:
#     if not num == 0:
#         counter += 1
#
# if counter == 0:
#     print(f"Mission was successful.")
# else:
#     print(f"Cupid has failed {counter} places.")
