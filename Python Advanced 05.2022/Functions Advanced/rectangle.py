def rectangle(length, width):

    if isinstance(length, str) and isinstance(width, str):
        return "Enter valid values!"

    elif isinstance(length, str) or isinstance(width, str):
        return "Enter valid values!"

    def area():
        rect_area = length * width
        return rect_area

    def perimeter():
        rect_perimeter = 2 * (length + width)
        return rect_perimeter

    result = f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

    return result


print(rectangle(2, 10))

print(rectangle('2', 10))
