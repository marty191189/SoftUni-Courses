import math

time_for_shooting = int(input())
number_of_scenes = int(input())
time_for_one_scene = int(input())

prep = (15 / 100) * time_for_shooting

time_for_shooting_all_scenes = number_of_scenes * time_for_one_scene

total_time_needed = prep + time_for_shooting_all_scenes

diff = abs(total_time_needed - time_for_shooting)

if time_for_shooting >= total_time_needed:
    print(f"You managed to finish the movie on time! You have {math.ceil(diff)} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {math.ceil(diff)} minutes.")
