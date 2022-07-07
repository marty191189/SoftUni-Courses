number_of_groups = int(input())

counter_musala = 0
counter_monblan = 0
counter_kili = 0
counter_k2 = 0
counter_everest = 0

total_people = 0

for group in range(1, number_of_groups + 1):

    people_in_group = int(input())

    total_people += people_in_group

    if people_in_group <= 5:
        counter_musala += people_in_group

    elif 6 <= people_in_group <= 12:
        counter_monblan += people_in_group

    elif 13 <= people_in_group <= 25:
        counter_kili += people_in_group

    elif 26 <= people_in_group <= 40:
        counter_k2 += people_in_group

    elif 41 <= people_in_group:
        counter_everest += people_in_group

perc_people_musala = (counter_musala / total_people) * 100
perc_people_monblan = (counter_monblan / total_people) * 100
perc_people_kili = (counter_kili / total_people) * 100
perc_people_k2 = (counter_k2 / total_people) * 100
perc_people_everest = (counter_everest / total_people) * 100

print(f"{perc_people_musala:.2f}%")
print(f"{perc_people_monblan:.2f}%")
print(f"{perc_people_kili:.2f}%")
print(f"{perc_people_k2:.2f}%")
print(f"{perc_people_everest:.2f}%")
