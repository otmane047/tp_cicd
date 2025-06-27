"""Module basic pour ubittest"""

from unittest import TestCase

from simple_math import SimpleMath


class TestSimpleMath(TestCase):
    """Test cases pour SimpleMath methods."""

    def test_add(self):
        """Test add method with various combinations.

        Tests positive numbers, negative numbers, zero, and larger numbers
        to ensure the add method works correctly in all cases.
        """

        assert SimpleMath.add(1, 2) == 3
        assert SimpleMath.add(-1, 1) == 0
        assert SimpleMath.add(0, 0) == 0
        assert SimpleMath.add(-5, -5) == -10
        assert SimpleMath.add(100, 200) == 300

    def test_subtract(self):
        """Test the subtract method with various combinations.

        Tests positive numbers, negative numbers, zero, and larger numbers
        to ensure the subtract method works correctly in all cases.
        """
        assert SimpleMath.subtract(5, 3) == 2
        assert SimpleMath.subtract(0, 0) == 0
        assert SimpleMath.subtract(-1, -1) == 0
        assert SimpleMath.subtract(10, 5) == 5
        assert SimpleMath.subtract(100, 50) == 50
