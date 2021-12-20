from task3 import num_of_couple
import unittest


class TestTask3(unittest.TestCase):

    def test_num(self):
        self.assertEqual(num_of_couple("1 2 1"), 1)
        self.assertEqual(num_of_couple("1 2 3 1 4 5 1"), 3)
        self.assertEqual(num_of_couple("1 1 8 7 1 3 2 1"), 6)

    def test_types(self):
        self.assertRaises(TypeError, num_of_couple, 5)
        self.assertRaises(TypeError, num_of_couple, 1.4)
        self.assertRaises(TypeError, num_of_couple, [1, 1, 1])
        self.assertRaises(TypeError, num_of_couple, {8, 3})
        self.assertRaises(TypeError, num_of_couple, (8, 3))
        self.assertRaises(TypeError, num_of_couple, True)
