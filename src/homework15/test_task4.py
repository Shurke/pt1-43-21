"""Tests for task4.py : Проект Эйлера. Задача 71.
"""

import unittest

from ddt import ddt, data, unpack
from task4 import gcd, simplify, search_left_numerator, StringWithoutSlash


@ddt
class TestEuler71(unittest.TestCase):

    @data([48, 80], [3, 9], [15, 75])
    @unpack
    def test_gcd(self, first_value, second_value):
        """Checking that the gcd function returns a number
        by which both arguments can be divisible without a remainder
        """
        nod = gcd(first_value, second_value)
        self.assertTrue(first_value/nod, first_value//nod)
        self.assertTrue(second_value/nod, second_value//nod)

    @data((48, 80), (3, 9), (15, 75))
    def test_simplify(self, value):
        """Checking that the simplify function returns a tuple
        of two integers.
        """
        result = simplify(value)
        self.assertIs(type(result), tuple)
        self.assertTrue(len(result) == 2)
        self.assertIs(type(result[0]), int)
        self.assertIs(type(result[1]), int)

    @data([100, "37"], [100, "3.7"])
    @unpack
    def test_fraction(self, first_value, second_value):
        """Testing that the second argument of the call
        to the search_left_numerator function should be a string of a fraction.
        Otherwise an exception will be thrown."""
        with self.assertRaises(StringWithoutSlash) as context:
            search_left_numerator(first_value, second_value)
        self.assertTrue("Второй аргумент вызова функции search_left_numerator "
                        "должен быть дробью." in str(context.exception))

    @data(["100", "200"], [100, "200"], ["100", 200])
    @unpack
    def test_type_notation_1(self, first_value, second_value):
        """Checking the type notation when calling functions
        with arguments of the wrong types.
        """
        self.assertRaises(TypeError, gcd, first_value, second_value)

    @data(100, "my string")
    def test_type_notation_2(self, value):
        """Checking the type notation when calling functions
        with arguments of the wrong types.
        """
        self.assertRaises(TypeError, simplify, value)

    @data(["100", "3/7"], [100.00, "3/7"])
    @unpack
    def test_type_notation_3(self, first_value, second_value):
        """Checking the type notation when calling functions
        with arguments of the wrong types.
        """
        self.assertRaises(TypeError, search_left_numerator, first_value, second_value)

    @data([100, 3 / 7], [100, 37])
    @unpack
    def test_type_notation_4(self, first_value, second_value):
        """Checking the type notation when calling functions
        with arguments of the wrong types.
        """
        self.assertRaises(AttributeError, search_left_numerator, first_value, second_value)

    @data([100, "37"])
    @unpack
    def test_type_notation_5(self, first_value, second_value):
        """Checking the type notation when calling functions
        with arguments of the wrong types.
        """
        self.assertRaises(StringWithoutSlash, search_left_numerator, first_value, second_value)


if __name__ == '__main__':
    unittest.main()
