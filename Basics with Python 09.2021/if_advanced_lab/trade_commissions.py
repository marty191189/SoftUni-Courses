city = input()
money_from_sale = float(input())
commission = 0

if city == "Sofia":
    if money_from_sale < 0:
        print("error")

    if 0 <= money_from_sale <= 500:
        commission = money_from_sale * 0.05
        print(f"{commission:.2f}")

    elif 500 < money_from_sale <= 1000:
        commission = money_from_sale * 0.07
        print(f"{commission:.2f}")

    elif 1000 < money_from_sale <= 10000:
        commission = money_from_sale * 0.08
        print(f"{commission:.2f}")

    elif 10000 < money_from_sale:
        commission = money_from_sale * 0.12
        print(f"{commission:.2f}")

elif city == "Varna":
    if money_from_sale < 0:
        print("error")

    if 0 <= money_from_sale <= 500:
        commission = money_from_sale * 0.045
        print(f"{commission:.2f}")

    elif 500 < money_from_sale <= 1000:
        commission = money_from_sale * 0.075
        print(f"{commission:.2f}")

    elif 1000 < money_from_sale <= 10000:
        commission = money_from_sale * 0.1
        print(f"{commission:.2f}")

    elif 10000 < money_from_sale:
        commission = money_from_sale * 0.13
        print(f"{commission:.2f}")

elif city == "Plovdiv":
    if money_from_sale < 0:
        print("error")

    if 0 <= money_from_sale <= 500:
        commission = money_from_sale * 0.055
        print(f"{commission:.2f}")

    elif 500 < money_from_sale <= 1000:
        commission = money_from_sale * 0.08
        print(f"{commission:.2f}")

    elif 1000 < money_from_sale <= 10000:
        commission = money_from_sale * 0.12
        print(f"{commission:.2f}")

    elif 10000 < money_from_sale:
        commission = money_from_sale * 0.145
        print(f"{commission:.2f}")

else:
    print("error")
