number_of_people = int(input())
list_of_wagons = list(map(int, input().split(" ")))

current_number_of_people = number_of_people

for wagon in range(len(list_of_wagons)):

    if list_of_wagons[wagon] == 0:

        if current_number_of_people >= 4:
            list_of_wagons[wagon] += 4
            current_number_of_people -= 4

        elif current_number_of_people < 4:
            list_of_wagons[wagon] += current_number_of_people
            current_number_of_people -= current_number_of_people

    elif 0 < list_of_wagons[wagon] <= 4:

        if current_number_of_people >= 4:
            diff = 4 - list_of_wagons[wagon]
            list_of_wagons[wagon] += diff
            current_number_of_people -= diff

        elif current_number_of_people < 4:

            if list_of_wagons[wagon] == 4:
                list_of_wagons[wagon] += 0

            elif list_of_wagons[wagon] < 4:
                list_of_wagons[wagon] += current_number_of_people
                current_number_of_people -= current_number_of_people

if (len(list_of_wagons) * 4) > sum(list_of_wagons):
    print(f"The lift has empty spots!")
    result = list(map(str, list_of_wagons))
    print(" ".join(result))

elif (len(list_of_wagons) * 4) == sum(list_of_wagons):
    if current_number_of_people > 0:
        print(f"There isn't enough space! {current_number_of_people} people in a queue!")
        result = list(map(str, list_of_wagons))
        print(" ".join(result))

    elif current_number_of_people == 0:
        result = list(map(str, list_of_wagons))
        print(" ".join(result))
