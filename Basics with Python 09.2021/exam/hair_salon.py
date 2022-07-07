target_money = int(input())

saved_money = 0

command = input()

while True:

    if command == "closed":
        break

    if command == "haircut":
        type_of_haircut = input()

        if type_of_haircut == "mens":
            saved_money += 15

        elif type_of_haircut == "ladies":
            saved_money += 20

        elif type_of_haircut == "kids":
            saved_money += 10

    elif command == "color":
        type_of_color = input()

        if type_of_color == "touch up":
            saved_money += 20

        elif type_of_color == "full color":
            saved_money += 30

    if saved_money >= target_money:
        print(f"You have reached your target for the day!")
        break

    command = input()

if target_money > saved_money:
    diff = abs(saved_money - target_money)
    print(f"Target not reached! You need {diff}lv. more.")

print(f"Earned money: {saved_money}lv.")
