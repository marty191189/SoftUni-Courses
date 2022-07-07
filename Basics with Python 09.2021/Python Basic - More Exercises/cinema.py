room_capacity = int(input())

price_of_ticket = 5
current_sum = 0
total_sum = 0

number_of_people = input()

while True:

    if number_of_people == "Movie time!":
        print(f"There are {room_capacity} seats left in the cinema.")
        break

    room_capacity -= int(number_of_people)

    if room_capacity < 0:
        print(f"The cinema is full.")
        break

    current_sum = int(number_of_people) * price_of_ticket
    total_sum += current_sum

    if int(number_of_people) % 3 == 0:
        total_sum = total_sum - 5

    number_of_people = input()

print(f"Cinema income - {total_sum} lv.")

# вярно решение
#
# room_capacity = int(input())
#
# price_of_ticket = 5
# current_sum = 0
# total_sum = 0
# seats_left = 0
#
# number_of_people = input()
#
# while number_of_people != "Movie time!":
#
#     room_capacity -= int(number_of_people)
#
#     if room_capacity < 0:
#         print(f"The cinema is full.")
#         break
#
#     current_sum = int(number_of_people) * price_of_ticket
#     total_sum += current_sum
#
#     if int(number_of_people) % 3 == 0:
#         total_sum = total_sum - 5
#
#     number_of_people = input()
#
# if room_capacity >= 0:
#     print(f"There are {room_capacity} seats left in the cinema.")
#
# print(f"Cinema income - {total_sum} lv.")
