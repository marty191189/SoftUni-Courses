fruit = input()
size_of_set = input()
number_of_sets = int(input())

total_sum = 0

if size_of_set == "small":

    if fruit == "Watermelon":
        total_sum += ((2 * 56) * number_of_sets)

    elif fruit == "Mango":
        total_sum += ((2 * 36.66) * number_of_sets)

    elif fruit == "Pineapple":
        total_sum += ((2 * 42.10) * number_of_sets)

    elif fruit == "Raspberry":
        total_sum += ((2 * 20) * number_of_sets)

elif size_of_set == "big":

    if fruit == "Watermelon":
        total_sum += ((5 * 28.70) * number_of_sets)

    elif fruit == "Mango":
        total_sum += ((5 * 19.60) * number_of_sets)

    elif fruit == "Pineapple":
        total_sum += ((5 * 24.80) * number_of_sets)

    elif fruit == "Raspberry":
        total_sum += ((5 * 15.20) * number_of_sets)

if 400 <= total_sum <= 1000:
    total_sum = total_sum - ((15 / 100) * total_sum)

elif 1000 < total_sum:
    total_sum = total_sum - ((50 / 100) * total_sum)

print(f"{total_sum:.2f} lv.")
