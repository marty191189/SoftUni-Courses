sq_m = float(input())

price = sq_m * 7.61

discount = ((18/100) * price)

final_price = price - discount

print(f"The final price is: {final_price} lv.")

print(f"The discount is: {discount} lv.")
