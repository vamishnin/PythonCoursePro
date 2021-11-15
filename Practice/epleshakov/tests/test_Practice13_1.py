import unittest
from Practice13_1 import to_roman, NonValidInput


class Test(unittest.TestCase):
    def test_to_roman(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(4673), 'MMMMDCLXXIII')
        self.assertEqual(to_roman(5000), 'MMMMM')

    def test_to_roman_negative(self):
        with self.assertRaises(NonValidInput):
            to_roman(0)
        with self.assertRaises(NonValidInput):
            to_roman(5001)
        with self.assertRaises(NonValidInput):
            to_roman('5001')


if __name__ == '__main__':
    unittest.main()
