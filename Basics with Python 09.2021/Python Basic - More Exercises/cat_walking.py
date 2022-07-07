minutes_walk_per_day = int(input())
number_of_walks = int(input())
cals_per_day = int(input())

total_walking_minutes = minutes_walk_per_day * number_of_walks

total_cals_burned = total_walking_minutes * 5

minimum_for_success = (50 / 100) * cals_per_day

if total_cals_burned >= minimum_for_success:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_cals_burned}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_cals_burned}.")
