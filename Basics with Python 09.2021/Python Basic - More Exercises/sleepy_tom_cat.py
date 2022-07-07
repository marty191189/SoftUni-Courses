number_of_free_days = int(input())

days_playing = 365 - number_of_free_days

actual_play_time = (days_playing * 63) + (number_of_free_days * 127)

diff = abs(30000 - actual_play_time)

hours = diff // 60

minutes = diff % 60

if 30000 >= actual_play_time:
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

else:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
