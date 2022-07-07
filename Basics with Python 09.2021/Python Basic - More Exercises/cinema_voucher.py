value_of_voucher = int(input())

sum_letters = 0
counter_tickets = 0
counter_other_goods = 0
price_of_purchased_item = 0

name_of_purchased_item = input()

while True:

    if name_of_purchased_item == "End":
        break

    if len(name_of_purchased_item) <= 8:

        first_letter = name_of_purchased_item[0]
        first_letter_as_number = ord(first_letter)

        price_of_purchased_item = first_letter_as_number

        if value_of_voucher >= price_of_purchased_item:

            value_of_voucher -= price_of_purchased_item

            counter_other_goods += 1

        else:
            break

    elif len(name_of_purchased_item) > 8:

        first_letter = name_of_purchased_item[0]
        first_letter_as_number = ord(first_letter)

        second_letter = name_of_purchased_item[1]
        second_letter_as_number = ord(second_letter)

        sum_letters = first_letter_as_number + second_letter_as_number

        price_of_purchased_item = sum_letters

        if value_of_voucher >= price_of_purchased_item:

            value_of_voucher -= price_of_purchased_item

            counter_tickets += 1

        else:
            break

    name_of_purchased_item = input()

print(counter_tickets)
print(counter_other_goods)
