import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(8, 4), 12)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8, 4), 4)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(8, 4), 32)
    def test_division(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        assert self.calc.divide(10, 0) is None
if __name__ == "__main__":
    unittest.main()