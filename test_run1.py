import unittest

class TestDuplicateDemo(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_addition_duplicate(self):
        self.assertEqual(1 + 1, 2)  # Duplicate

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_subtraction_duplicate(self):
        self.assertEqual(5 - 3, 2)  # Duplicate

if __name__ == '__main__':
    unittest.main()
