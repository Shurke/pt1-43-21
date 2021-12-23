""" test task3

Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами.
Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится
‘assertRaises’. Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама.
"""

from task3 import add_range
from task3 import get_ranges

from ddt import data
from ddt import ddt
from ddt import unpack

import unittest


@ddt
class TestGetRanges(unittest.TestCase):
    """Test cases for the get_ranges() function."""

    @data([1, "n", 5, 6, 7, 8])
    def test_bad_input(self, user_input):
        """Test for bad input."""
        self.failUnlessRaises(ValueError, get_ranges(user_input))

    @data(
        ([1, 4, 5, 6, 7, 8], "1, 4-8"),
        ([4], "4"),
        ([0, 1, 2, 3, 4, 7, 8, 10], "0-4, 7-8, 10"),
        ([3, 5, 7], "3, 5, 7"),
    )
    @unpack
    def test_output(self, user_input, output):
        """Test for proper output."""
        self.assertEqual(get_ranges(user_input), output)


@ddt
class TestAddRange(unittest.TestCase):

    @data(
        ("", 2, 2, "2"),
        ("", 3, 7, "3-7"),
        ("4-6", 9, 9, "4-6, 9"),
        ("4-6", 9, 15, "4-6, 9-15"))
    @unpack
    def test_output(self, string_of_ranges, first_number, middle_number, output):
        self.assertEqual(add_range(string_of_ranges, first_number, middle_number), output)


if __name__ == '__main__':
    unittest.main()
