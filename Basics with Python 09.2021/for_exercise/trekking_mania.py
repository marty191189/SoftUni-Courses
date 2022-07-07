number_of_groups = int(input())
all_people = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(1, number_of_groups + 1):
    people_in_group = int(input())
    all_people += people_in_group

    if people_in_group <= 5:
        p1 += people_in_group

    elif 6 <= people_in_group <= 12:
        p2 += people_in_group

    elif 13 <= people_in_group <= 25:
        p3 += people_in_group

    elif 26 <= people_in_group <= 40:
        p4 += people_in_group

    elif 41 <= people_in_group:
        p5 += people_in_group

final_p1 = (p1 / all_people) * 100
final_p2 = (p2 / all_people) * 100
final_p3 = (p3 / all_people) * 100
final_p4 = (p4 / all_people) * 100
final_p5 = (p5 / all_people) * 100

print(f"{final_p1:.2f}%")
print(f"{final_p2:.2f}%")
print(f"{final_p3:.2f}%")
print(f"{final_p4:.2f}%")
print(f"{final_p5:.2f}%")
