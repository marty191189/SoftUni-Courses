class Circle:

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = float(new_radius)

    def get_area(self):
        result = (self.radius**2) * Circle.pi
        return result

    def get_circumference(self):
        result = 2 * self.radius * Circle.pi
        return result


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
