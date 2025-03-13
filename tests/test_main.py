import pytest
from src.main import add, subtract, multiply

def test_add():
    assert add(1, 2) == 3
    with pytest.raises(TypeError):
        add(1, '2')

def test_subtract():
    assert subtract(1, 2) == -1
    with pytest.raises(TypeError):
        subtract(1, '2')

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(2,'2') == '22'
    assert multiply('1',2) == '1'*2