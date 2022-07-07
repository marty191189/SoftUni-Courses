import math

figure = input()

if figure == "square":
    a = float(input())
    area = a * a
    print(f"Area = {area:.3f}")

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"Area = {area:.3f}")

elif figure == "circle":
    r = float(input())
    area = r * r * math.pi
    print(f"Area = {area:.3f}")

else:
    print("Това е триъгълник")
    a = float(input())
    h = float(input())
    area = (a * h) / 2
    print(f"Area = {area:.3f}")
