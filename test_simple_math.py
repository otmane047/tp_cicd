
from unittest import TestCase


class TestSimpleMath(TestCase):
    def test_add(self):
        from simple_math import SimpleMath
        assert SimpleMath.add(1, 2) == 3
        assert SimpleMath.add(-1, 1) == 0
        assert SimpleMath.add(0, 0) == 0
        assert SimpleMath.add(-5, -5) == -10
        assert SimpleMath.add(100, 200) == 300