stadium_capacity = int(input())
number_of_fans = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for fan in range(1, number_of_fans + 1):
    sector = input()

    if sector == "A":
        p1 += 1

    elif sector == "B":
        p2 += 1

    elif sector == "V":
        p3 += 1

    elif sector == "G":
        p4 += 1

final_p1_percent = (p1 / number_of_fans) * 100
final_p2_percent = (p2 / number_of_fans) * 100
final_p3_percent = (p3 / number_of_fans) * 100
final_p4_percent = (p4 / number_of_fans) * 100
final_p5_percent = (number_of_fans / stadium_capacity) * 100

print(f"{final_p1_percent:.2f}%")
print(f"{final_p2_percent:.2f}%")
print(f"{final_p3_percent:.2f}%")
print(f"{final_p4_percent:.2f}%")
print(f"{final_p5_percent:.2f}%")
