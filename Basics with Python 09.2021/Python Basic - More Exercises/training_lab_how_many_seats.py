import math

h = float(input())
w = float(input())

w1 = w * 100
h1 = h * 100
corridor = 100

usable_space = w1 - corridor

rows = math.floor(usable_space / 70)
places = math.floor(h1 / 120)
work_places = (rows * places) - 3

print(work_places)
