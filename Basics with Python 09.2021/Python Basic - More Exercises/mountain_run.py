import math

record_in_seconds = float(input())
distance_in_metres = float(input())
time_for_going_up_one_m_in_seconds = float(input())

normal_time = (distance_in_metres * time_for_going_up_one_m_in_seconds)

setback_in_seconds = math.floor(distance_in_metres / 50) * 30

total_time = normal_time + setback_in_seconds

diff = abs(total_time - record_in_seconds)

if record_in_seconds > total_time:
    print(f"Yes! The new record is {total_time:.2f} seconds.")

else:
    print(f"No! He was {diff:.2f} seconds slower.")
