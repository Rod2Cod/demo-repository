from src.circle import circle
from math import pi
import pytest


class Test_circle:
    def setup_method(self,method):
        print(f'setup{method}')
        self.circle = circle(1)

    def teardown_method(self,method):
        print(f'teardown{method}')
        del self.circle

    def test_area(self):
        assert self.circle.area() == pi

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * pi

    def test_radius(self):
        assert self.circle.radius == 1

    def test_area_type_error(self):
        c = circle('1')
        with pytest.raises(TypeError):
            c.area()

    def test_perimeter_type_error(self):
        c = circle('1')
        with pytest.raises(TypeError):
            c.perimeter()