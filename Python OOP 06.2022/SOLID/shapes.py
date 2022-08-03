from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def find_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def find_area(self):
        return self.width * self.height


class Square(Shape):

    def __init__(self, width):
        self.width = width

    def find_area(self):
        return self.width ** 2


class Triangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def find_area(self):
        return (self.width * self.height) / 2


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.find_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print(f"The total area is: {calculator.total_area}")
