import unittest
import BasicCalculator

class UseCases(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(BasicCalculator.addition(10, 5), "num1 + num2 = 15\n")

    def test_subtraction(self):
        self.assertEqual(BasicCalculator.subtraction(10, 5), "num1 - num2 = 5\n")

    def test_multiplication(self):
        self.assertEqual(BasicCalculator.multiplication(10, 5), "num1 * num2 = 50\n")

    def test_division(self):
        self.assertEqual(BasicCalculator.division(10, 5), "num1 / num2 = 2.0\n") 

    def test_square_root(self):
        self.assertEqual(BasicCalculator.square_root(10, 5), "Square root of num1 = 3.1622776601683795\nSquare root of num2 = 2.23606797749979\n") 

    def test_power(self):
        self.assertEqual(BasicCalculator.power(10, 5), "num1 to the power of num2 = 100000.0\n") 

if __name__ == '__main__':
    unittest.main()