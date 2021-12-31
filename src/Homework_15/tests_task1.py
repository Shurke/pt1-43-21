"""
Module for testing task1 Homework_15
"""

import unittest

from ddt import data
from ddt import ddt
from ddt import unpack

from task1 import Enemy
from task1 import Hero


@ddt
class TestClasses(unittest.TestCase):
    """Test case for task1"""
    @data((1, 1, 1), (2, 1, 3), (5, 5, 5))
    @unpack
    def tests_for_hero_class_create(self, *args):
        """The test check, that 'inst' is instance of class 'Hero'"""
        inst = Hero(*args)
        self.assertIsInstance(inst, Hero)

    @data((1, 1, 1), (1, 2, 3))
    @unpack
    def tests_for_enemy_class_create(self, *args):
        """The test check, that 'inst' (instance of Enemy class) is not instance of class 'Hero'"""
        inst = Enemy(*args)
        self.assertNotIsInstance(inst, Hero)

    @data(('a', 1, 1), ([], 'c', 1), (1, 1, {'a': 1}))
    @unpack
    def tests_with_incorrect_input_data(self, *args):
        """The test raises an exception when entering incorrect data"""
        with self.assertRaises(TypeError) as error:
            Hero(*args)
            self.assertEqual('Incorrect input: characteristic must be a integer!',
                             error.exception.args[0])

    @data((-1, 1, 1), (1, -1, 1), (1, 1, -1))
    @unpack
    def tests_with_negative_integer(self, *args):
        """The test raises an exception when entering negative number """
        with self.assertRaises(TypeError) as error:
            Hero(*args)
            self.assertEqual("Characteristics can't be less than 0!", error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
