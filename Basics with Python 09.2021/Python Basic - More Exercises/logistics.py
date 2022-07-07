number_of_loads = int(input())

p1 = 0
p2 = 0
p3 = 0

average_price_ton_load = 0
final_bus_percent = 0
final_truck_percent = 0
final_train_percent = 0

total_tonnage_all_loads = 0

price_all_loads_bus = 0
price_all_loads_truck = 0
price_all_loads_train = 0

price_per_ton_bus = 200
price_per_ton_truck = 175
price_per_ton_train = 120

for load in range(number_of_loads):
    tonnage_of_load = int(input())
    total_tonnage_all_loads += tonnage_of_load

    if tonnage_of_load <= 3:
        p1 += tonnage_of_load

    elif 4 <= tonnage_of_load <= 11:
        p2 += tonnage_of_load

    elif 12 <= tonnage_of_load:
        p3 += tonnage_of_load

average_price_ton_load = ((p1 * price_per_ton_bus) + (p2 * price_per_ton_truck) + (p3 * price_per_ton_train)) / total_tonnage_all_loads

final_bus_percent = (p1 / total_tonnage_all_loads) * 100
final_truck_percent = (p2 / total_tonnage_all_loads) * 100
final_train_percent = (p3 / total_tonnage_all_loads) * 100

print(f"{average_price_ton_load:.2f}")

print(f"{final_bus_percent:.2f}%")
print(f"{final_truck_percent:.2f}%")
print(f"{final_train_percent:.2f}%")
