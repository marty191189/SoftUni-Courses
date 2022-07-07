number_of_moves = int(input())
points = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0

for move in range(1, number_of_moves + 1):
    number = int(input())

    if 0 <= number <= 9:
        points += ((20 / 100) * number)
        p1 += 1

    elif 10 <= number <= 19:
        points += ((30 / 100) * number)
        p2 += 1

    elif 20 <= number <= 29:
        points += ((40 / 100) * number)
        p3 += 1

    elif 30 <= number <= 39:
        points += 50
        p4 += 1

    elif 40 <= number <= 50:
        points += 100
        p5 += 1

    else:
        points /= 2
        p6 += 1

final_p1_percent = (p1 / number_of_moves) * 100
final_p2_percent = (p2 / number_of_moves) * 100
final_p3_percent = (p3 / number_of_moves) * 100
final_p4_percent = (p4 / number_of_moves) * 100
final_p5_percent = (p5 / number_of_moves) * 100
final_p6_percent = (p6 / number_of_moves) * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {final_p1_percent:.2f}%")
print(f"From 10 to 19: {final_p2_percent:.2f}%")
print(f"From 20 to 29: {final_p3_percent:.2f}%")
print(f"From 30 to 39: {final_p4_percent:.2f}%")
print(f"From 40 to 50: {final_p5_percent:.2f}%")
print(f"Invalid numbers: {final_p6_percent:.2f}%")
