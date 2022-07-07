number_of_visitors = int(input())

counter_back = 0
counter_chest = 0
counter_legs = 0
counter_abs = 0
counter_protein_shake = 0
counter_protein_bar = 0

for visitor in range(1, number_of_visitors + 1):

    activity = input()

    if activity == "Back":
        counter_back += 1

    elif activity == "Chest":
        counter_chest += 1

    elif activity == "Legs":
        counter_legs += 1

    elif activity == "Abs":
        counter_abs += 1

    elif activity == "Protein shake":
        counter_protein_shake += 1

    elif activity == "Protein bar":
        counter_protein_bar += 1

perc_work_out = ((counter_back + counter_chest + counter_legs + counter_abs) / number_of_visitors) * 100
perc_protein = ((counter_protein_shake + counter_protein_bar) / number_of_visitors) * 100

print(f"{counter_back} - back")
print(f"{counter_chest} - chest")
print(f"{counter_legs} - legs")
print(f"{counter_abs} - abs")
print(f"{counter_protein_shake} - protein shake")
print(f"{counter_protein_bar} - protein bar")
print(f"{perc_work_out:.2f}% - work out")
print(f"{perc_protein:.2f}% - protein")
