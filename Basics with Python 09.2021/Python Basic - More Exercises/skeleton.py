minutes_control_time = int(input())
seconds_control_time = int(input())
distance_in_meters = float(input())
seconds_time_to_travel_100_meters = int(input())

total_control_time_in_seconds = (minutes_control_time * 60) + seconds_control_time

number_discounted_time = distance_in_meters / 120

total_discounted_time = number_discounted_time * 2.5

his_time = (distance_in_meters / 100) * seconds_time_to_travel_100_meters - total_discounted_time

if his_time <= total_control_time_in_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {his_time:.3f}.")

else:
    diff = abs(total_control_time_in_seconds - his_time)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
