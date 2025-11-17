import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(6, 4), 24)
        self.assertEqual(mul(-2, -9), 18)
        self.assertEqual(mul(-3, 5), -15)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 8), 4)
        self.assertEqual(div(5, -45), -9)
        self.assertAlmostEqual(div(3, 1), (1/3))
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(7, -24), 25)
        self.assertEqual(hypotenuse(-8, -15), 17)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
            square_root(-16)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(25), 5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()