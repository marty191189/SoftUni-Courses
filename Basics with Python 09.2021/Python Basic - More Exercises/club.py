target = float(input())
profit = 0
check = 0

while True:

    if profit >= target:
        break

    cocktail = input()

    if cocktail == "Party!":
        check = 1
        break

    amount = int(input())
    price = len(cocktail)
    type_profit = price * amount

    if type_profit % 2 != 0:
        type_profit = type_profit - ((25 / 100) * type_profit)

    profit += type_profit

diff = abs(target - profit)

if check == 1:
    print(f'We need {diff:.2f} leva more.')
    print(f'Club income - {profit:.2f} leva.')

elif target <= profit:
    print(f'Target acquired.')
    print(f'Club income - {profit:.2f} leva.')

# вярно решение

# target = float(input())
# profit = 0
# check = 0
#
# while profit < target:
#     cocktail = input()
#
#     if cocktail == "Party!":
#         check = 1
#         break
#
#     amount = int(input())
#     price = len(cocktail)
#     type_profit = price * amount
#
#     if type_profit % 2 != 0:
#         type_profit *= 0.75
#
#     profit += type_profit
#
# diff = abs(target - profit)
#
# if check == 1:
#     print(f'We need {diff:.2f} leva more.')
#     print(f'Club income - {profit:.2f} leva.')
#
# elif target <= profit:
#     print(f'Target acquired.')
#     print(f'Club income - {profit:.2f} leva.')
