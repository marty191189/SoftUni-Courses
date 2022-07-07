import math

height_of_wall = int(input())
width_of_wall = int(input())
percent_not_for_painting = int(input())

total_area = height_of_wall * width_of_wall * 4

area_for_painting = math.ceil(total_area - ((percent_not_for_painting / 100) * total_area))

litres_of_paint = input()

while True:

    if litres_of_paint == "Tired!":
        print(f"{area_for_painting} quadratic m left.")
        break

    area_for_painting = area_for_painting - int(litres_of_paint)

    if area_for_painting == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break

    elif area_for_painting < 0:
        paint_left = abs(area_for_painting)
        print(f"All walls are painted and you have {paint_left} l paint left!")
        break

    litres_of_paint = input()
