"""Tests for calculator module."""

import pytest
from src.calculator import add, subtract, multiply, divide, calculate_average


class TestAddition:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_add_mixed_numbers(self):
        assert add(-1, 1) == 0


class TestSubtraction:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_resulting_negative(self):
        assert subtract(3, 5) == -2


class TestMultiplication:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivision:
    """Tests for the divide function."""

    def test_divide_evenly(self):
        assert divide(10, 2) == 5

    def test_divide_with_remainder(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestAverage:
    """Tests for the calculate_average function."""

    def test_average_of_list(self):
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0

    def test_average_single_number(self):
        assert calculate_average([5]) == 5.0

    # ⚠️ INTENTIONAL BUG: This test will fail!
    # We expect 2.5 but the list actually averages to 2.0
    def test_average_intentional_failure(self):
        """This test has a bug - wrong expected value."""
        result = calculate_average([1, 2, 3])
        assert result == 2.0, f"Expected 2.0 but got {result}"
