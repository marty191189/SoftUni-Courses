name_of_film = input()
type_of_package = input()
number_of_tickets = int(input())

total_sum = 0

if name_of_film == "John Wick":

    if type_of_package == "Drink":
        total_sum = number_of_tickets * 12

    elif type_of_package == "Popcorn":
        total_sum = number_of_tickets * 15

    elif type_of_package == "Menu":
        total_sum = number_of_tickets * 19

elif name_of_film == "Star Wars":

    if type_of_package == "Drink":
        total_sum = number_of_tickets * 18

    elif type_of_package == "Popcorn":
        total_sum = number_of_tickets * 25

    elif type_of_package == "Menu":
        total_sum = number_of_tickets * 30

    if number_of_tickets >= 4:
        total_sum = total_sum - ((30 / 100) * total_sum)

elif name_of_film == "Jumanji":

    if type_of_package == "Drink":
        total_sum = number_of_tickets * 9

    elif type_of_package == "Popcorn":
        total_sum = number_of_tickets * 11

    elif type_of_package == "Menu":
        total_sum = number_of_tickets * 14

    if number_of_tickets == 2:
        total_sum = total_sum - ((15 / 100) * total_sum)

print(f"Your bill is {total_sum:.2f} leva.")
