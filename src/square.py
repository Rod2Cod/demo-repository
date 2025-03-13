from .shape import shape

class square(shape):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side of square should be greater than 0")
        self.side = side

    def area(self) -> float:
        return float(self.side ** 2)

    def perimeter(self) -> float:
        return float(4 * self.side)