import pytest
from mathcalculator import MathCalculator_bracken576

def test_addition():
    calc = MathCalculator_bracken576()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtraction():
    calc = MathCalculator_bracken576()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0

def test_multiplication():
    calc = MathCalculator_bracken576()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6

def test_division():
    calc = MathCalculator_bracken576()
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5

def test_division_by_zero():
    calc = MathCalculator_bracken576()
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calc.divide(5, 0)