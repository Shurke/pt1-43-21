from task4 import num_of_nat_fract
import unittest


class TestTask4(unittest.TestCase):

    def test_num(self):
        self.assertEqual(num_of_nat_fract(8), 21)
        self.assertEqual(num_of_nat_fract(2), 1)
        self.assertEqual(num_of_nat_fract(10), 31)

    def test_values(self):
        self.assertRaises(ValueError, num_of_nat_fract, -2)
        self.assertRaises(ValueError, num_of_nat_fract, -5)

    def test_types(self):
        self.assertRaises(TypeError, num_of_nat_fract, 5 + 2j)
        self.assertRaises(TypeError, num_of_nat_fract, 1.4)
        self.assertRaises(TypeError, num_of_nat_fract, "Восемь")
        self.assertRaises(TypeError, num_of_nat_fract, [8, 3])
        self.assertRaises(TypeError, num_of_nat_fract, True)


if __name__ == '__main__':
    unittest.main()
