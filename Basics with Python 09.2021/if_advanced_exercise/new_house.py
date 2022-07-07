type_of_flower = input()
number_of_flower = int(input())
budget = int(input())

roses = 5
dahlias = 3.80
tulips = 2.80
narcissus = 3
gladiolus = 2.50

total_sum = 0

if type_of_flower == "Roses":
    if number_of_flower > 80:
        total_sum = number_of_flower * roses
        total_sum = total_sum - ((10 / 100) * total_sum)

    else:
        total_sum = number_of_flower * roses

elif type_of_flower == "Dahlias":
    if number_of_flower > 90:
        total_sum = number_of_flower * dahlias
        total_sum = total_sum - ((15 / 100) * total_sum)

    else:
        total_sum = number_of_flower * dahlias

elif type_of_flower == "Tulips":
    if number_of_flower > 80:
        total_sum = number_of_flower * tulips
        total_sum = total_sum - ((15 / 100) * total_sum)

    else:
        total_sum = number_of_flower * tulips

elif type_of_flower == "Narcissus":
    if number_of_flower < 120:
        total_sum = number_of_flower * narcissus
        total_sum = total_sum + ((15 / 100) * total_sum)

    else:
        total_sum = number_of_flower * narcissus

elif type_of_flower == "Gladiolus":
    if number_of_flower < 80:
        total_sum = number_of_flower * gladiolus
        total_sum = total_sum + ((20 / 100) * total_sum)

    else:
        total_sum = number_of_flower * gladiolus

diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flower} {type_of_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
