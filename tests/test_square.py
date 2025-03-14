import src.square as sq
import pytest
from time import sleep

class TestSquare:
    def setup_method(self):
        self.sq = sq.square(5)
    
    def teardown_method(self):
        del self.sq

    def test_area(self):
        assert self.sq.area() == 25
    
    def test_perimeter(self):
        assert self.sq.perimeter() == 20
    
    def test_area_type(self):
        assert type(self.sq.area()) == float

    def test_perimeter_type(self):
        assert type(self.sq.perimeter()) == float

    def test_area_value(self):
        with pytest.raises(ValueError):
            s = sq.square(-5)
            s.area()

    def test_perimeter_value(self):
        with pytest.raises(ValueError):
            s = sq.square(-5)
            s.perimeter()

    @pytest.mark.skip(reason="Very inefficient")
    @pytest.mark.slow
    def test_unefficient(self):
        sleep(5)
        assert True