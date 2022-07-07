number_of_pvc = int(input())
size_of_pvc = input()
type_of_delivery = input()

total_sum = 0

if size_of_pvc == "90X130":
    total_sum = number_of_pvc * 110

    if 30 < number_of_pvc < 60:
        total_sum = total_sum - ((5 / 100) * total_sum)

        if type_of_delivery == "With delivery":
            total_sum += 60

        elif type_of_delivery == "Without delivery":
            total_sum = total_sum

    elif 60 < number_of_pvc:
        total_sum = total_sum - ((8 / 100) * total_sum)

        if type_of_delivery == "With delivery":
            total_sum += 60

        elif type_of_delivery == "Without delivery":
            total_sum = total_sum

if size_of_pvc == "100X150":
    total_sum = number_of_pvc * 140

    if 40 < number_of_pvc < 80:
        total_sum = total_sum - ((6 / 100) * total_sum)

        if type_of_delivery == "With delivery":
            total_sum += 60

        elif type_of_delivery == "Without delivery":
            total_sum = total_sum

    elif 80 < number_of_pvc:
        total_sum = total_sum - ((10 / 100) * total_sum)

        if type_of_delivery == "With delivery":
            total_sum += 60

        elif type_of_delivery == "Without delivery":
            total_sum = total_sum

elif size_of_pvc == "130X180":
    total_sum = number_of_pvc * 190

    if 20 < number_of_pvc < 50:
        total_sum = total_sum - ((7 / 100) * total_sum)

        if type_of_delivery == "With delivery":
            total_sum += 60

        elif type_of_delivery == "Without delivery":
            total_sum = total_sum

    elif 50 < number_of_pvc < 99:
        total_sum = total_sum - ((12 / 100) * total_sum)

        if type_of_delivery == "With delivery":
            total_sum += 60

        elif type_of_delivery == "Without delivery":
            total_sum = total_sum

elif size_of_pvc == "200X300":
    total_sum = number_of_pvc * 250

    if 25 < number_of_pvc < 50:
        total_sum = total_sum - ((9 / 100) * total_sum)

        if type_of_delivery == "With delivery":
            total_sum += 60

        elif type_of_delivery == "Without delivery":
            total_sum = total_sum

    elif 50 < number_of_pvc:
        total_sum = total_sum - ((14 / 100) * total_sum)

        if type_of_delivery == "With delivery":
            total_sum += 60

        elif type_of_delivery == "Without delivery":
            total_sum = total_sum

if number_of_pvc > 99:
    total_sum = total_sum - ((4 / 100) * total_sum)

if number_of_pvc < 10:
    print("Invalid order")
else:
    print(f"{total_sum:.2f} BGN")
