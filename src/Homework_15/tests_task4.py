"""
Module for testing task4 Homework_15
"""


import unittest
from task4 import task4


class TestCaseTask4(unittest.TestCase):
    """Tests for task4 module"""
    def test_1(self):
        """
        Test for one integer
        :return: OK
        """
        self.assertEqual(task4(510510), 'n = 510510; max n/Euler(n) = 5.539388020833333')

    def test_2(self):
        """
        Test for iter object for 1 to 8
        :return: OK
        """
        self.assertEqual(task4([1, 2, 3, 4, 5, 6, 7, 8]), 'n = 6; max n/Euler(n) = 3.0')

    def test_3(self):
        """
        Test for iter object from 1 to 8 in reverse order
        :return: OK
        """
        self.assertEqual(task4([8, 7, 6, 5, 4, 3, 2, 1]), 'n = 6; max n/Euler(n) = 3.0')

    def test_4(self):
        """
        Test for two integer in tuple
        :return: OK
        """
        self.assertEqual(task4((30030, 510510)), 'n = 510510; max n/Euler(n) = 5.539388020833333')

    def test_5(self):
        """
        Test raise call's if type of iterable is not list or tuple
        :return:
        """
        with self.assertRaises(TypeError) as error:
            task4({100000, 1000020, 1000011})
            self.assertEqual("The type of the iterable must be 'list' or 'tuple'",
                             error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
