"""
Module for testing task3 Homework_15
"""


import unittest
from task3 import task2


class TestCaseTask3(unittest.TestCase):
    """Tests for task2 function"""

    def test_1(self):
        """Passed test :return: OK"""
        self.assertEqual(task2(('Odessa', 'Moscow', 'Novgorod'),
                               {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                                2: 'Ukraine Kiev Donetsk Odessa'}), 'Ukraine Russia Russia')

    def test_2(self):
        """Passed test. :return: OK"""
        self.assertEqual(task2(('Brest', 'NewYork'),
                               {1: 'Belarus Minsk Gomel Brest',
                                2: 'USA Washington NewYork LosAngeles'}), 'Belarus USA')

    def test_3(self):
        """Test with raise call. If the city name contains a number, an exception is thrown and
        the corresponding message is displayed"""
        with self.assertRaises(TypeError) as error:
            task2(('Ode1ssa', 'Moscow', 'Novgorod'),
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual('The city name cannot contain numbers!', error.exception.args[0])

    def test_4(self):
        """Test with raise call: if an invalid key is used as an argument when passing a
        dictionary"""
        with self.assertRaises(TypeError) as error:
            task2(('Odessa', 'Moscow', 'Novgorod'),
                  {'key': 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual('The key in dictionary must be a integer!', error.exception.args[0])

    def test_5(self):
        """Test with raise call: if the first place of the list is not a country"""
        with self.assertRaises(TypeError) as error:
            task2(('Odessa', 'Moscow', 'Novgorod'),
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Kiev Donetsk Odessa'})
        self.assertEqual('The name of the country should be in the first place!',
                         error.exception.args[0])

    def test_6(self):
        """Test with raise call: if the city or country name does not start with a capital letter
        in dictionary"""
        with self.assertRaises(TypeError) as error:
            task2(('Odessa', 'Moscow', 'Novgorod'),
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine kiev Donetsk Odessa'})
        self.assertEqual('City and country name must start with a capital letter',
                         error.exception.args[0])

    def test_7(self):
        """Test with raise call. If the city name does not start with a capital letter in
        request list"""
        with self.assertRaises(TypeError) as error:
            task2(('Odessa', 'moscow', 'Novgorod'),
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual('City name must start with a capital letter', error.exception.args[0])

    def test_8(self):
        """Test with raise call: checks the value of the argument types :return: OK"""
        with self.assertRaises(TypeError) as error:
            task2({'Odessa', 'Moscow', 'Novgorod'},
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual("Data contained request with cities for check transmits in function with"
                         " 'tuple' or 'list' type!", error.exception.args[0])

    def test_9(self):
        """Test with raise call: checks the value of the argument types :return: OK"""
        with self.assertRaises(TypeError) as error:
            task2(('Odessa', 'Moscow', 'Novgorod'),
                  [1, 'Russia Moscow Petersburg Novgorod Kaluga',
                   2, 'Ukraine Kiev Donetsk Odessa'])
        self.assertEqual("You need to pass to the function a dictionary!",
                         error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
