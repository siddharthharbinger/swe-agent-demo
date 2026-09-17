import unittest
from calc import calculate_offset, multiply, subtract


class TestCalculator(unittest.TestCase):
    def test_calculate_offset(self):
        # calculate_offset(10, 5) should equal 15 (currently returns 5)
        self.assertEqual(calculate_offset(10, 5), 15)
        self.assertEqual(calculate_offset(20, 3), 23)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)


if __name__ == '__main__':
    unittest.main()
