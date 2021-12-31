"""
Module for testing task4 Homework_15
"""

import task4
import unittest


class TestCaseTask4(unittest.TestCase):
    """Tests for task4 module"""
    def test_1_with_correct_data_input(self):
        """It's a correct test receives correct input data and outputs the result """
        self.assertEqual(task4.max_euler(10), (6, 3.0))

    def test_2_with_any_correct_data_input(self):
        """It's is a correct test receives correct input data and outputs the result """
        self.assertEqual(task4.max_euler(50000), (30030, 5.213541666666667))

    def test_3_with_any_correct_data_input(self):
        """It's is a correct test receives correct input data and outputs the result """
        self.assertEqual(task4.max_euler(520000), (510510, 5.539388020833333))

    def test_4_with_str_data_type_input(self):
        """Test raise call's if type of input data are not integer"""
        with self.assertRaises(TypeError) as error:
            task4.max_euler('a')
            self.assertEqual('Please enter a simple integer!', error.exception.args[0])

    def test_5_with_float_data_type_input(self):
        """Test raise call's if type of input data are not integer"""
        with self.assertRaises(TypeError) as error:
            task4.max_euler(2.5555)
            self.assertEqual('Please enter a simple integer!', error.exception.args[0])

    def test_5_with_function_as_data_input(self):
        """Test raise call's if type of input data are not integer"""
        with self.assertRaises(TypeError) as error:
            task4.max_euler(task4.euler())
            self.assertEqual('Please enter a simple integer!', error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
