number_of_days = int(input())
type_of_room = input()
grade = input()

number_of_nights = number_of_days - 1
mid_price = 0
total_price = 0

price_room_for_one_person = 18
price_apartment = 25
price_president_apartment = 35

if type_of_room == "room for one person":
    mid_price = number_of_nights * price_room_for_one_person

elif type_of_room == "apartment":
    if number_of_nights < 10:
        base_price = number_of_nights * price_apartment
        mid_price = base_price - ((30 / 100) * base_price)

    elif 10 <= number_of_nights <= 15:
        base_price = number_of_nights * price_apartment
        mid_price = base_price - ((35 / 100) * base_price)

    elif 15 < number_of_nights:
        base_price = number_of_nights * price_apartment
        mid_price = base_price - ((50 / 100) * base_price)

elif type_of_room == "president apartment":
    if number_of_nights < 10:
        base_price = number_of_nights * price_president_apartment
        mid_price = base_price - ((10 / 100) * base_price)

    elif 10 <= number_of_nights <= 15:
        base_price = number_of_nights * price_president_apartment
        mid_price = base_price - ((15 / 100) * base_price)

    elif 15 < number_of_nights:
        base_price = number_of_nights * price_president_apartment
        mid_price = base_price - ((20 / 100) * base_price)

if grade == "positive":
    total_price = mid_price + ((25 / 100) * mid_price)

elif grade == "negative":
    total_price = mid_price - ((10 / 100) * mid_price)

print(f"{total_price:.2f}")
