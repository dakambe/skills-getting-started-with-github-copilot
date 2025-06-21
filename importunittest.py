import unittest
from letslearnpy import add_numbers

# FILE: test_letslearnpy.py


class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(5, 10), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -10), -15)

    def test_add_positive_and_negative(self):
        self.assertEqual(add_numbers(10, -5), 5)

    def test_add_with_zero(self):
        self.assertEqual(add_numbers(0, 10), 10)
        self.assertEqual(add_numbers(10, 0), 10)

    def test_add_floating_point_numbers(self):
        self.assertAlmostEqual(add_numbers(5.5, 4.5), 10.0)

    def test_add_large_numbers(self):
        self.assertEqual(add_numbers(1000, 2000), 3000)

    def test_add_same_numbers(self):
        self.assertEqual(add_numbers(10, 10), 20)

    def test_add_different_positive_numbers(self):
        self.assertEqual(add_numbers(10, 30), 40)

if __name__ == "__main__":
    unittest.main()

