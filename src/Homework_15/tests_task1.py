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
    @data((1, 1, 1, 1), (2, 1, 3, 1), (5, 5, 5, 1))
    @unpack
    def test_1(self, *args):
        """The test check, that 'inst' is instance of class 'Hero'"""
        inst = Hero(*args)
        self.assertIsInstance(inst, Hero)

    @data((1, 1, 1, 1), (1, 2, 3, 1))
    @unpack
    def test_2(self, *args):
        """The test check, that 'inst' (instance of Enemy class) is not instance of class 'Hero'"""
        inst = Enemy(*args)
        self.assertNotIsInstance(inst, Hero)

    @data(('a', 1, 1, 1, 1), (1, 2, [], 'c', 1))
    @unpack
    def test_3(self, *args):
        """The test raises an exception when entering incorrect data"""
        with self.assertRaises(TypeError) as error:
            Hero(*args)
            self.assertEqual('Incorrect input: characteristic must be a integer!',
                             error.exception.args[0])

    @data((-1, 1, 1, 1, -1), (1, 1, -1, 1, 2))
    @unpack
    def test_4(self, *args):
        """The test raises an exception when entering negative number """
        with self.assertRaises(TypeError) as error:
            Hero(*args)
            self.assertEqual("Characteristics can't be less than 0!", error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
