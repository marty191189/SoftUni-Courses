import math

number_magnolii = int(input())
number_zumbuli = int(input())
number_roses = int(input())
number_kaktusi = int(input())
price_present = float(input())

magnolii = 3.25
zumbuli = 4
roses = 3.50
kaktusi = 8

total_sum = (magnolii * number_magnolii) + (zumbuli * number_zumbuli) + (roses * number_roses) + (kaktusi * number_kaktusi)

total_sum = total_sum - ((5 / 100) * total_sum)

diff = abs(price_present - total_sum)

if total_sum >= price_present:
    print(f"She is left with {math.floor(diff)} leva.")

else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")
