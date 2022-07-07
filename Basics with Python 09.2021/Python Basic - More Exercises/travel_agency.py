name_of_city = input()
type_of_package = input()
vip_discount = input()
number_of_days = int(input())

total_sum = 0

if name_of_city != "Bansko" and name_of_city != "Borovets" and name_of_city != "Varna" and name_of_city != "Burgas":
    print(f"Invalid input!")

elif type_of_package != "withEquipment" and type_of_package != "noEquipment" and type_of_package != "withBreakfast" and type_of_package != "noBreakfast":
    print(f"Invalid input!")

elif number_of_days < 1:
    print(f"Days must be positive number!")

else:
    if name_of_city == "Bansko":

        if type_of_package == "withEquipment":

            total_sum = 100

            if vip_discount == "yes":
                total_sum = total_sum - ((10 / 100) * total_sum)

            if number_of_days > 7:
                total_sum = total_sum * (number_of_days - 1)

            else:
                total_sum = total_sum * number_of_days

        elif type_of_package == "noEquipment":

            total_sum = 80

            if vip_discount == "yes":
                total_sum = total_sum - ((5 / 100) * total_sum)

            if number_of_days > 7:
                total_sum = total_sum * (number_of_days - 1)

            else:
                total_sum = total_sum * number_of_days

    elif name_of_city == "Borovets":

        if type_of_package == "withEquipment":
            total_sum = 100

            if vip_discount == "yes":
                total_sum = total_sum - ((10 / 100) * total_sum)

            if number_of_days > 7:
                total_sum = total_sum * (number_of_days - 1)

            else:
                total_sum = total_sum * number_of_days

        elif type_of_package == "noEquipment":
            total_sum = 80

            if vip_discount == "yes":
                total_sum = total_sum - ((5 / 100) * total_sum)

            if number_of_days > 7:
                total_sum = total_sum * (number_of_days - 1)

            else:
                total_sum = total_sum * number_of_days

    elif name_of_city == "Varna":

        if type_of_package == "withBreakfast":

            total_sum = 130

            if vip_discount == "yes":
                total_sum = total_sum - ((12 / 100) * total_sum)
            if number_of_days > 7:
                total_sum = total_sum * (number_of_days - 1)

            total_sum = total_sum * number_of_days

        elif type_of_package == "noBreakfast":

            total_sum = 100

            if vip_discount == "yes":
                total_sum = total_sum - ((7 / 100) * total_sum)

            if number_of_days > 7:
                total_sum = total_sum * (number_of_days - 1)

            else:
                total_sum = total_sum * number_of_days

    elif name_of_city == "Burgas":

        if type_of_package == "withBreakfast":

            total_sum = 130

            if vip_discount == "yes":
                total_sum = total_sum - ((12 / 100) * total_sum)

            if number_of_days > 7:
                total_sum = total_sum * (number_of_days - 1)

            else:
                total_sum = total_sum * number_of_days

        elif type_of_package == "noBreakfast":

            total_sum = 100

            if vip_discount == "yes":
                total_sum = total_sum - ((7 / 100) * total_sum)

            if number_of_days > 7:
                total_sum = total_sum * (number_of_days - 1)

            else:
                total_sum = total_sum * number_of_days

    print(f"The price is {total_sum:.2f}lv! Have a nice time!")
