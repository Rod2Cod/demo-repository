from .shape import shape
from math import pi

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * pi * self.radius