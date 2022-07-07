target_sum = int(input())

price_of_item = input()

saved_money_cc = 0
saved_money_cs = 0
saved_money_all = 0

counter = 0
counter_cc = 0
counter_cs = 0

while True:

    counter += 1

    if price_of_item == "End":
        print("Failed to collect required money for charity.")
        break

    price_of_item_int = int(price_of_item)

    if counter % 2 == 0:
        if price_of_item_int < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            counter_cc += 1
            saved_money_cc += price_of_item_int
            saved_money_all += price_of_item_int

    else:
        if price_of_item_int > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            counter_cs += 1
            saved_money_cs += price_of_item_int
            saved_money_all += price_of_item_int

    if saved_money_all >= target_sum:
        average_cs = (saved_money_cs / counter_cs)
        average_cc = (saved_money_cc / counter_cc)
        print(f"Average CS: {average_cs:.2f}")
        print(f"Average CC: {average_cc:.2f}")
        break

    price_of_item = input()

# второ вярно решение

# target_sum = int(input())
#
# price_of_item = input()
#
# saved_money_cc = 0
# saved_money_cs = 0
# saved_money_all = 0
#
# counter = 0
# counter_cc = 0
# counter_cs = 0
#
# while True:
#
#     counter += 1
#
#     if price_of_item == "End":
#         print("Failed to collect required money for charity.")
#         break
#
#     price_of_item_int = int(price_of_item)
#
#     if counter % 2 == 1:
#         if price_of_item_int > 100:
#             print("Error in transaction!")
#         else:
#             print("Product sold!")
#             counter_cs += 1
#             saved_money_cs += price_of_item_int
#             saved_money_all += price_of_item_int
#
#     else:
#         if price_of_item_int < 10:
#             print("Error in transaction!")
#         else:
#             print("Product sold!")
#             counter_cc += 1
#             saved_money_cc += price_of_item_int
#             saved_money_all += price_of_item_int
#
#     if saved_money_all >= target_sum:
#         average_cs = (saved_money_cs / counter_cs)
#         average_cc = (saved_money_cc / counter_cc)
#         print(f"Average CS: {average_cs:.2f}")
#         print(f"Average CC: {average_cc:.2f}")
#         break
#
#     price_of_item = input()
