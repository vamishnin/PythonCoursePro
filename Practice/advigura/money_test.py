# from unittest import TestCase
import unittest
from money import Money 



class TestMoney(unittest.TestCase):
    
    def test_equal(self):
        self.assertTrue(Money(2, 3) == Money(2, 3))
        # self.assertFalse(Money(6, 3) == Money(2, 3))
    
    def test_lt(self):
        self.assertTrue(Money(1, 0), Money(2, 0))
        
    def test_add(self):
        self.assertEqual(Money(1, 0) + Money(2, 0), Money(3, 0))
        
    def test_sub(self):
        self.assertEqual(Money(5, 1) - Money(2, 9), Money(2, 92))
        
    def test_truediv(self):
        self.assertEqual(Money(3, 0) / Money(3, 0), 1)
        
    def test_convert_to_dollar(self):
        self.assertEqual(Money(140, 0).convert_to_dollar(), Money(2, 0))

if __name__ == '__main__': 
    unittest.main()

