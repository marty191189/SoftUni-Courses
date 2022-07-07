month = input()
number_of_nights = int(input())

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65

    if number_of_nights <= 7:
        total_apartment_price = number_of_nights * apartment_price
        total_studio_price = number_of_nights * studio_price
        print(f"Apartment: {total_apartment_price:.2f} lv.")
        print(f"Studio: {total_studio_price:.2f} lv.")

    elif 7 < number_of_nights < 14:
        studio_price = studio_price - ((5 / 100) * studio_price)

        total_apartment_price = number_of_nights * apartment_price
        total_studio_price = number_of_nights * studio_price
        print(f"Apartment: {total_apartment_price:.2f} lv.")
        print(f"Studio: {total_studio_price:.2f} lv.")

    elif number_of_nights > 14:
        studio_price = studio_price - ((30 / 100) * studio_price)
        apartment_price = apartment_price - ((10 / 100) * apartment_price)

        total_apartment_price = number_of_nights * apartment_price
        total_studio_price = number_of_nights * studio_price
        print(f"Apartment: {total_apartment_price:.2f} lv.")
        print(f"Studio: {total_studio_price:.2f} lv.")

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70

    if number_of_nights <= 14:
        total_apartment_price = number_of_nights * apartment_price
        total_studio_price = number_of_nights * studio_price
        print(f"Apartment: {total_apartment_price:.2f} lv.")
        print(f"Studio: {total_studio_price:.2f} lv.")

    elif number_of_nights > 14:
        studio_price = studio_price - ((20 / 100) * studio_price)
        apartment_price = apartment_price - ((10 / 100) * apartment_price)

        total_apartment_price = number_of_nights * apartment_price
        total_studio_price = number_of_nights * studio_price
        print(f"Apartment: {total_apartment_price:.2f} lv.")
        print(f"Studio: {total_studio_price:.2f} lv.")

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

    if number_of_nights <= 14:
        total_apartment_price = number_of_nights * apartment_price
        total_studio_price = number_of_nights * studio_price
        print(f"Apartment: {total_apartment_price:.2f} lv.")
        print(f"Studio: {total_studio_price:.2f} lv.")

    elif number_of_nights > 14:
        apartment_price = apartment_price - ((10 / 100) * apartment_price)

        total_apartment_price = number_of_nights * apartment_price
        total_studio_price = number_of_nights * studio_price
        print(f"Apartment: {total_apartment_price:.2f} lv.")
        print(f"Studio: {total_studio_price:.2f} lv.")
