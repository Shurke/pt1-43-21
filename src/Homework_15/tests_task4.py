"""
Module for testing task4 Homework_15
"""


import unittest
from task4 import _euler
from task4 import max_euler


class TestCaseTask4(unittest.TestCase):
    """Tests for task4 module"""
    def test_1(self):
        """It's a correct test receives correct input data and outputs the result """
        self.assertEqual(max_euler(10), (6, 3.0))

    def test_2(self):
        """It's is a correct test receives correct input data and outputs the result """
        self.assertEqual(max_euler(50000), (30030, 5.213541666666667))

    def test_3(self):
        """It's is a correct test receives correct input data and outputs the result """
        self.assertEqual(max_euler(520000), (510510, 5.539388020833333))

    def test_4(self):
        """Test raise call's if type of input data are not integer"""
        with self.assertRaises(TypeError) as error:
            max_euler('a')
            self.assertEqual('Please enter a simple integer!', error.exception.args[0])

    def test_5(self):
        """Test raise call's if type of input data are not integer"""
        with self.assertRaises(TypeError) as error:
            max_euler(2.5555)
            self.assertEqual('Please enter a simple integer!', error.exception.args[0])

    def test_6(self):
        """Test raise call's if type of input data are not integer"""
        with self.assertRaises(TypeError) as error:
            max_euler(_euler())
            self.assertEqual('Please enter a simple integer!', error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
