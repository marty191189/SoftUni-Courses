inherited_money = float(input())
year_he_dies = int(input())

living_expenses = 0
diff = 0
current_year = 1799
current_age = 17

for year in range(1799, year_he_dies):
    current_year += 1
    current_age += 1

    if current_year % 2 == 0:
        living_expenses = 12000
        inherited_money -= living_expenses

    elif current_year % 2 != 0:
        living_expenses = (12000 + (current_age * 50))
        inherited_money -= living_expenses

diff = abs(inherited_money)

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")

else:
    print(f"He will need {diff:.2f} dollars to survive.")

# heritage_money = float(input())
# year = int(input())
# money_spent = 0
#
# for num in range(1800, year + 1):
#     if num % 2 == 0:
#         money_spent += 12000
#     elif num % 2 != 0:
#         diff = abs(year - num)
#         money_spent += 12000 + 50 * (18 + num - 1800)
#
# diff = abs(heritage_money - money_spent)
#
# if heritage_money >= money_spent:
#     print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
# else:
#     print(f"He will need {diff:.2f} dollars to survive.")
