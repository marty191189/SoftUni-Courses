season = input()
km_for_month = float(input())

salary_before_taxes = 0
salary_after_taxes = 0

if season == "Spring" or season == "Autumn":
    if km_for_month <= 5000:
        salary_before_taxes = 0.75 * km_for_month

    elif 5000 < km_for_month <= 10000:
        salary_before_taxes = 0.95 * km_for_month

    elif 10000 < km_for_month <= 20000:
        salary_before_taxes = 1.45 * km_for_month

elif season == "Summer":
    if km_for_month <= 5000:
        salary_before_taxes = 0.90 * km_for_month

    elif 5000 < km_for_month <= 10000:
        salary_before_taxes = 1.10 * km_for_month

    elif 10000 < km_for_month <= 20000:
        salary_before_taxes = 1.45 * km_for_month

elif season == "Winter":
    if km_for_month <= 5000:
        salary_before_taxes = 1.05 * km_for_month

    elif 5000 < km_for_month <= 10000:
        salary_before_taxes = 1.25 * km_for_month

    elif 10000 < km_for_month <= 20000:
        salary_before_taxes = 1.45 * km_for_month

salary_before_taxes = salary_before_taxes * 4

salary_after_taxes = salary_before_taxes - ((10 / 100) * salary_before_taxes)

print(f"{salary_after_taxes:.2f}")
