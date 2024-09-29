import pytest
from adder.adder import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_not_correctly(self):
        assert self.calc.multiply(self, 2, 2) != 44

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 3) == 2

    def test_division_calculate_correctly(self):
        with pytest.raises(ValueError, match="Cannot divide by zero!"):
            assert self.calc.division(self, 6, 0)

    def test_division_calculate_not_correctly(self):
        assert self.calc.division(self, 6, 3) != 0

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_subtraction_calculate_not_correctly(self):
        assert self.calc.subtraction(self, 2, 2) != 1

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_adding_calculate_not_correctly(self):
        assert self.calc.adding(self, 2, 2) != 5