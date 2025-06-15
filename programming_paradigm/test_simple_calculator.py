import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---- ADDITION TESTS ----
    def test_addition(self):
        """Test addition with normal and edge cases."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, 5), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    # ---- SUBTRACTION TESTS ----
    def test_subtraction(self):
        """Test subtraction with normal and edge cases."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    # ---- MULTIPlication TESTS ----
    def test_multiplication(self):
        """Test multiplication with normal and edge cases."""
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    # ---- DIVISION TESTS ----
    def test_division(self):
        """Test division with normal and division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(5, 0))  # Should return None


if __name__ == '__main__':
    unittest.main()
