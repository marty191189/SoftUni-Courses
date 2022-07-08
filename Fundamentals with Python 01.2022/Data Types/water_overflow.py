# number_of_refills = int(input())
#
# capacity = 255
#
# water_in_tank = 0
#
# tank_is_full = False
#
# for i in range(1, number_of_refills + 1):
#     refill = int(input())
#
#     if capacity > refill:
#         capacity -= refill
#         water_in_tank += refill
#
#     elif capacity == refill:
#         capacity -= refill
#         water_in_tank += refill
#         tank_is_full = True
#
#     elif capacity < refill:
#         capacity = 0
#         water_in_tank = 0
#         tank_is_full = True
#
#     if tank_is_full:
#         print("Insufficient capacity!")
#
# print(water_in_tank)

number_of_lines = int(input())

capacity = 0

for i in range(1, number_of_lines + 1):
    litres_of_water = int(input())

    if litres_of_water + capacity <= 255:
        capacity += litres_of_water
        continue

    print("Insufficient capacity!")

print(capacity)
