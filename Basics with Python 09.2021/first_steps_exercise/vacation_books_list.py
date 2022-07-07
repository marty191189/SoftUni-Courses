import math

number_of_pages = int(input())
number_of_pages_for_one_hour = int(input())
number_of_days = int(input())

total_time_reading = number_of_pages / number_of_pages_for_one_hour

hours_needed = total_time_reading / number_of_days

print(math.floor(hours_needed))
