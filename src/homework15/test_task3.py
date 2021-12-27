"""Tests for task3.py."""

import unittest

from ddt import data
from ddt import ddt
from task3 import word_count


@ddt
class TestWordCount(unittest.TestCase):

    @data(1000, [1, 2], ("string 1", "string 2"))
    def test_type_notation(self, value):
        """Checking the execution of the function (getting an exception)

        'word_count' when it is called with an argument of the wrong type.
        """
        self.assertRaises(AttributeError, word_count, value)

    def test_type_return_value(self):
        """Checking that the 'word_count' function returns an integer."""
        result = word_count("Это тестовая строка для подсчета \n в ней количества слов.")
        self.assertIs(type(result), int)


if __name__ == '__main__':
    unittest.main()
