import math

loze_sq_m = int(input())
grozde_1_sq_m = float(input())
needed_litres_wine = int(input())
number_workers = int(input())

harvest = loze_sq_m * grozde_1_sq_m

usable_grozde = (40 / 100) * harvest

total_wine = usable_grozde / 2.5

diff = abs(needed_litres_wine - total_wine)

liters_per_person = diff / number_workers

if total_wine >= needed_litres_wine:
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(liters_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
