import math

name_series = input()
duration_episode = int(input())
duration_break = int(input())

time_for_lunch = (1 / 8) * duration_break

time_for_relax = (1 / 4) * duration_break

usable_time = duration_break - time_for_lunch - time_for_relax

diff = abs(duration_episode - usable_time)

if duration_episode <= usable_time:
    print(f"You have enough time to watch {name_series} and left with {math.ceil(diff)} minutes free time.")

else:
    print(f"You don't have enough time to watch {name_series}, you need {math.ceil(diff)} more minutes.")
