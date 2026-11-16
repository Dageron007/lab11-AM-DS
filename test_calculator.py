# https://github.com/Dageron007/lab11-AM-DS
# Partner 1: Danila Sterlev
# Partner 2: Anthony Mitromaras
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 2), -2)
        self.assertEqual(add(0, 7), 7)

    def test_subtract(self):
        self.assertEqual(subtract(7, 3), 4)
        self.assertEqual(subtract(3, 7), -4)
        self.assertEqual(subtract(5, 5), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,6),3.0)
        self.assertEqual(div(4,8), 2.0)
        self.assertEqual(div(-2,8), -4.0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(4, 2), 0.5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
