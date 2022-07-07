name = input()

points = 0

name_winner = ""
points_winner = 0

while True:

    if name == "Stop":
        break

    for letter in name:

        current_letter = ord(letter)

        number = int(input())

        if current_letter == number:
            points += 10

        else:
            points += 2

    if points >= points_winner:
        points_winner = points
        name_winner = name

    current_letter = 0
    points = 0

    name = input()

print(f"The winner is {name_winner} with {points_winner} points!")
