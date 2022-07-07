target_height = int(input())

target_is_reached = False
starting_height = target_height - 30
counter_failed_jumps_on_same_height = 0
counter_all_jumps = 0

while counter_failed_jumps_on_same_height != 3:

    current_attempt_in_metres = int(input())

    counter_all_jumps += 1

    if current_attempt_in_metres > target_height and starting_height >= target_height:
        target_is_reached = True
        break

    elif current_attempt_in_metres > starting_height:
        starting_height += 5
        counter_failed_jumps_on_same_height = 0

    else:
        counter_failed_jumps_on_same_height += 1

if target_is_reached or starting_height > target_height:
    print(f"Tihomir succeeded, he jumped over {starting_height}cm after {counter_all_jumps} jumps.")
else:
    print(f"Tihomir failed at {starting_height}cm after {counter_all_jumps} jumps.")
