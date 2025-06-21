import unittest
from letslearnpy import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -15), -20)

    def test_positive_and_negative(self):
        self.assertEqual(add_numbers(-5, 15), 10)

    def test_with_zero(self):
        self.assertEqual(add_numbers(0, 10), 10)
        self.assertEqual(add_numbers(10, 0), 10)

    def test_floats(self):
        self.assertAlmostEqual(add_numbers(2.5, 3.5), 6.0)
        self.assertAlmostEqual(add_numbers(-1.1, 1.1), 0.0)

if __name__ == "__main__":
    unittest.main()