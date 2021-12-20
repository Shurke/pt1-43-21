import unittest
from task3 import task2


class TestCaseTask3(unittest.TestCase):
    """Tests for task2 function"""
    def test_1(self):
        self.assertEqual(task2(('Odessa', 'Moscow', 'Novgorod'),
                               {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                                2: 'Ukraine Kiev Donetsk Odessa'}), 'Ukraine Russia Russia')

    def test_2(self):
        self.assertEqual(task2(('Brest', 'NewYork'),
                               {1: 'Belarus Minsk Gomel Brest',
                                2: 'USA Washington NewYork LosAngeles'}), 'Belarus USA')

    def test_3(self):
        with self.assertRaises(TypeError) as e:
            task2(('Ode1ssa', 'Moscow', 'Novgorod'),
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual('The city name cannot contain numbers!', e.exception.args[0])

    def test_4(self):
        with self.assertRaises(TypeError) as e:
            task2(('Odessa', 'Moscow', 'Novgorod'),
                  {'key': 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual('The key in dictionary must be a integer!', e.exception.args[0])

    def test_5(self):
        with self.assertRaises(TypeError) as e:
            task2(('Odessa', 'Moscow', 'Novgorod'),
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Kiev Donetsk Odessa'})
        self.assertEqual('The name of the country should be in the first place!',
                         e.exception.args[0])

    def test_6(self):
        with self.assertRaises(TypeError) as e:
            task2(('Odessa', 'Moscow', 'Novgorod'),
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine kiev Donetsk Odessa'})
        self.assertEqual('City and country name must start with a capital letter',
                         e.exception.args[0])

    def test_7(self):
        with self.assertRaises(TypeError) as e:
            task2(('Odessa', 'moscow', 'Novgorod'),
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual('City name must start with a capital letter', e.exception.args[0])

    def test_8(self):
        with self.assertRaises(TypeError) as e:
            task2({'Odessa', 'Moscow', 'Novgorod'},
                  {1: 'Russia Moscow Petersburg Novgorod Kaluga',
                   2: 'Ukraine Kiev Donetsk Odessa'})
        self.assertEqual("Data contained request with cities for check transmits in function with"
                         " 'tuple' or 'list' type!", e.exception.args[0])

    def test_9(self):
        with self.assertRaises(TypeError) as e:
            task2(('Odessa', 'Moscow', 'Novgorod'), [1, 'Russia Moscow Petersburg Novgorod Kaluga',
                                                     2, 'Ukraine Kiev Donetsk Odessa'])
        self.assertEqual("You need to pass to the function a dictionary!", e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
