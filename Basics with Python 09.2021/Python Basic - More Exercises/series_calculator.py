import math

name_of_series = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
duration_of_episode_no_ads = float(input())

duration_of_ads = (20 / 100) * duration_of_episode_no_ads

duration_of_episode_with_ads = duration_of_episode_no_ads + duration_of_ads

special_episodes = number_of_seasons * 10

time_needed = duration_of_episode_with_ads * number_of_episodes * number_of_seasons + special_episodes

print(f"Total time needed to watch the {name_of_series} series is {math.floor(time_needed)} minutes.")
