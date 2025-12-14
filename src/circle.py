from figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius can't be less than 0")
        self.radius = radius

    def get_area(self):
        return pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * pi * self.radius