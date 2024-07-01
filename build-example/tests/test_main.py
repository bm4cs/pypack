import unittest
from packaging_example import main

class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        result = main.add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_multiply_numbers(self):
        result = main.multiply_numbers(2, 3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()