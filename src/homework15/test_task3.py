""" test task3

Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами.
Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится
‘assertRaises’. Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама.
"""


from task3 import get_ranges
from task3 import add_range
import unittest


class Testgetranges(unittest.TestCase):
    """Test cases for the get_ranges() function."""

    def test_bad_input(self):
        """Test for bad input."""
        user_input = [1, "n", 5, 6, 7, 8]
        self.assertIsNone(get_ranges(user_input))

    def test_output(self):
        """Test for proper output."""
        user_input = [1, 4, 5, 6, 7, 8]
        output = "1, 4-8"
        self.assertEqual(get_ranges(user_input), output)
        user_input = [4]
        output = "4"
        self.assertEqual(get_ranges(user_input), output)
        user_input = [0, 1, 2, 3, 4, 7, 8, 10]
        output = "0-4, 7-8, 10"
        self.assertEqual(get_ranges(user_input), output)
        user_input = [3, 5, 7]
        output = "3, 5, 7"
        self.assertEqual(get_ranges(user_input), output)


class Testaddrange(unittest.TestCase):

    def test_output(self):
        string_of_ranges = ""
        first_number = 2
        middle_number = 2
        output = "2"
        self.assertEqual(add_range(string_of_ranges, first_number, middle_number), output)

        string_of_ranges = ""
        first_number = 3
        middle_number = 7
        output = "3-7"
        self.assertEqual(add_range(string_of_ranges, first_number, middle_number), output)

        string_of_ranges = "4-6"
        first_number = 9
        middle_number = 9
        output = "4-6, 9"
        self.assertEqual(add_range(string_of_ranges, first_number, middle_number), output)

        string_of_ranges = "4-6"
        first_number = 9
        middle_number = 15
        output = "4-6, 9-15"
        self.assertEqual(add_range(string_of_ranges, first_number, middle_number), output)


if __name__ == '__main__':
    unittest.main()
