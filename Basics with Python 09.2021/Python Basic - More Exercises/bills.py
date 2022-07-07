number_of_months = int(input())

water_price = 20
internet_price = 15
water_bill = 0
internet_bill = 0
bill_sum_for_other = 0
other_bills = 0
electricity_price = 0
average_all_expenses_for_month = 0

for month in range(number_of_months):
    electricity_price += float(input())

    water_bill = water_price * number_of_months
    internet_bill = internet_price * number_of_months

    bill_sum_for_others = (electricity_price + water_bill + internet_bill)
    other_bills = bill_sum_for_others + ((20 / 100) * bill_sum_for_others)
    average_all_expenses_for_month = (electricity_price + water_bill + internet_bill + other_bills) / number_of_months

print(f"Electricity: {electricity_price:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average_all_expenses_for_month:.2f} lv")
