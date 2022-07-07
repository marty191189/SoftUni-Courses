length = float(input())
width = float(input())
height = float(input())
percent = float(input())

volume = length * width * height

volume_in_litres = volume / 1000

percent_needed = percent / 100

litres_needed = volume_in_litres * (1 - percent_needed)

print(litres_needed)
