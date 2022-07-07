season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())

sport = None
price_all_nights = 0

if type_of_group == "boys" or type_of_group == "girls":
    if season == "Winter":
        price_all_nights = 9.60 * number_of_nights * number_of_students

    elif season == "Spring":
        price_all_nights = 7.20 * number_of_nights * number_of_students

    elif season == "Summer":
        price_all_nights = 15 * number_of_nights * number_of_students

elif type_of_group == "mixed":
    if season == "Winter":
        price_all_nights = 10 * number_of_nights * number_of_students

    elif season == "Spring":
        price_all_nights = 9.50 * number_of_nights * number_of_students

    elif season == "Summer":
        price_all_nights = 20 * number_of_nights * number_of_students

if 10 <= number_of_students < 20:
    price_all_nights = price_all_nights - ((5 / 100) * price_all_nights)

elif 20 <= number_of_students < 50:
    price_all_nights = price_all_nights - ((15 / 100) * price_all_nights)

elif 50 <= number_of_students:
    price_all_nights = price_all_nights - ((50 / 100) * price_all_nights)

if type_of_group == "girls":
    if season == "Winter":
        sport = "Gymnastics"

    elif season == "Spring":
        sport = "Athletics"

    elif season == "Summer":
        sport = "Volleyball"

elif type_of_group == "boys":
    if season == "Winter":
        sport = "Judo"

    elif season == "Spring":
        sport = "Tennis"

    elif season == "Summer":
        sport = "Football"

elif type_of_group == "mixed":
    if season == "Winter":
        sport = "Ski"

    elif season == "Spring":
        sport = "Cycling"

    elif season == "Summer":
        sport = "Swimming"

print(f"{sport} {price_all_nights:.2f} lv.")
