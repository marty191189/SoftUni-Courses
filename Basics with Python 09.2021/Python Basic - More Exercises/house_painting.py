x_height_house = float(input())
y_length_house = float(input())
h_height_triangle_wall_roof = float(input())

# BACK AND FRONT AND SIDEWALL

back_wall_area = (x_height_house * x_height_house)

front_wall_area = ((x_height_house * x_height_house) - (1.2 * 2))

side_wall_area = 2 * ((x_height_house * y_length_house) - (1.5 * 1.5))

sum_front_and_side_area = back_wall_area + front_wall_area + side_wall_area

# ROOF

rectangle_roof_area = 2 * (x_height_house * y_length_house)

triangle_roof_area = 2 * ((x_height_house * h_height_triangle_wall_roof) / 2)

sum_area_roof = rectangle_roof_area + triangle_roof_area

litres_green_paint_needed = (sum_front_and_side_area / 3.4)

litres_red_paint_needed = (sum_area_roof / 4.3)

print(f"{litres_green_paint_needed:.2f}")
print(f"{litres_red_paint_needed:.2f}")
