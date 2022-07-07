pocket_money = float(input())
money_for_one_day = float(input())
expenses = float(input())
price_of_gift = float(input())

pocket_money = pocket_money * 5

money_from_shop = money_for_one_day * 5

total_saved_money = pocket_money + money_from_shop

total_saved_money = total_saved_money - expenses

diff = abs(price_of_gift - total_saved_money)

if total_saved_money >= price_of_gift:
    print(f"Profit: {total_saved_money:.2f} BGN, the gift has been purchased.")

else:
    print(f"Insufficient money: {diff:.2f} BGN.")
