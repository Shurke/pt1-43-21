"""
Module for testing task3 Homework_15
"""

import task3
import unittest


class TestCaseTask3(unittest.TestCase):
    """Tests for task2 function"""

    def test_with_correct_input_data(self):
        """Passed test :return: OK"""
        self.assertEqual(task3.task2(('Odessa', 'Moscow', 'Novgorod'),
                                     {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                                      2: 'Ukraine Kiev Donetsk Odessa'}), 'Ukraine Russia Russia')

    def test_with_any_correct_input_data(self):
        """Passed test. :return: OK"""
        self.assertEqual(task3.task2(('Brest', 'NewYork'),
                                     {1: 'Belarus Minsk Gomel Brest',
                                      2: 'USA Washington NewYork LosAngeles'}), 'Belarus USA')

    def test_with_number_in_city_names_in_request(self):
        """If the city name contains a number, an exception is thrown"""
        with self.assertRaises(TypeError) as error:
            task3.task2(('Ode1ssa', 'Moscow', 'Novgorod'),
                        {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                         2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual('The city name cannot contain numbers!', error.exception.args[0])

    def test_with_incorrect_data_in_dictionary(self):
        """if the city name doesn't start with a capital letter an exception is thrown"""
        with self.assertRaises(TypeError) as error:
            task3.task2(('Odessa', 'Moscow', 'Novgorod'),
                        {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                         2: 'Ukraine kiev Donetsk Odessa'})
        self.assertEqual('City and country names must be longer than 1, start with'
                         ' a capital letter, and contain only letters.', error.exception.args[0])

    def test_with_lowercase_name_start_in_request(self):
        """If the city name doesn't start with a capital letter in list raise called"""
        with self.assertRaises(TypeError) as error:
            task3.task2(('Odessa', 'moscow', 'Novgorod'),
                        {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                         2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual('City name must start with a capital letter', error.exception.args[0])

    def test_with_incorrect_data_type_in_request(self):
        """Test with raise call: checks the value of the argument types :return: OK"""
        with self.assertRaises(TypeError) as error:
            task3.task2({'Odessa', 'Moscow', 'Novgorod'},
                        {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                         2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual("Incorrect input data type!", error.exception.args[0])

    def test_with_incorrect_data_type_in_dictionary(self):
        """Test with raise call: checks the value of the argument types :return: OK"""
        with self.assertRaises(TypeError) as error:
            task3.task2(('Odessa', 'Moscow', 'Novgorod'),
                        [1, 'Russia Moscow Petersburg Novgorod Kaluga',
                         2, 'Ukraine Kiev Donetsk Odessa'])
        self.assertEqual("Incorrect input data type!", error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
