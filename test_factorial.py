from __future__ import division
import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_fails_on_no_args(self):
        with self.assertRaises(TypeError):
            factorial()

    def test_fails_on_three_args(self):
        with self.assertRaises(TypeError):
            factorial(1, 2, 3)

    def test_fails_on_two_args(self):
        with self.assertRaises(TypeError):
            factorial(1, 2)

    def test_fails_on_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_one_for_same(self):
        result = factorial(3)
        self.assertEqual(result, 6)

    def test_result_is_float(self):
        result = factorial(1.0)
        self.assertIs(type(result), type(1.0))

    def test_result_is_int(self):
        result = factorial(1)
        self.assertIs(type(result), type(1))

    def test_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_10(self):
        result = factorial(10)
        self.assertEqual(result, 3628800)

if __name__ == '__main__':
    unittest.main()
