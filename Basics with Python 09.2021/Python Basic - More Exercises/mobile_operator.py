duration_contract = input()
type_of_contract = input()
included_internet = input()
number_months_using_service = int(input())

price_contract = 0

if duration_contract == "one":

    if type_of_contract == "Small":
        price_contract = 9.98

    elif type_of_contract == "Middle":
        price_contract = 18.99

    elif type_of_contract == "Large":
        price_contract = 25.98

    elif type_of_contract == "ExtraLarge":
        price_contract = 35.99

elif duration_contract == "two":

    if type_of_contract == "Small":
        price_contract = 8.58

    elif type_of_contract == "Middle":
        price_contract = 17.09

    elif type_of_contract == "Large":
        price_contract = 23.59

    elif type_of_contract == "ExtraLarge":
        price_contract = 31.79

if included_internet == "yes":

    if price_contract <= 10:
        price_contract += 5.50

    elif price_contract <= 30:
        price_contract += 4.35

    elif price_contract > 30:
        price_contract += 3.85

total_sum = price_contract * number_months_using_service

if duration_contract == "two":
    total_sum = total_sum - ((3.75 / 100) * total_sum)

print(f"{total_sum:.2f} lv.")
