'''Tests for task4'''

import unittest
from task4 import great_comm_divisor, max_m, modulo_inverse_list, mutually_simple_list, sum_func
import pytest


class TestGreatCommDivisor(unittest.TestCase):
    def test_great(self):
        self.assertEqual(great_comm_divisor(10, 20), 10)
        self.assertEqual(great_comm_divisor(144, 136), 8)
        self.assertEqual(great_comm_divisor(123, 1246), 1)
        self.assertEqual(great_comm_divisor(-9, 8), 1)
        self.assertEqual(great_comm_divisor(8, -9), 1)
        with self.assertRaises(TypeError):
            great_comm_divisor('a', 'b')

    def test_mutually_simple_list(self):
        self.assertEqual(
            mutually_simple_list(15),
            [1, 2, 4, 7, 8, 11, 13, 14])
        with self.assertRaises(TypeError):
            mutually_simple_list('str')

    def test_modulo_inverse_list(self):
        self.assertEqual(
            modulo_inverse_list([1, 2, 4, 7, 8, 11, 13, 14], 15),
            [1, 4, 11]
        )
        with self.assertRaises(TypeError):
            modulo_inverse_list(1)

    def test_max_m(self):
        self.assertEqual(max_m(15), 11)
        self.assertEqual(max_m(100), 51)
        self.assertEqual(max_m(7), 1)
        with self.assertRaises(TypeError):
            max_m('a')

    def test_sum_func(self):
        self.assertEqual(sum_func([7, 15, 100]), 63)

    @pytest.mark.parametrize('n', ['a', 1.1, {'a': 3}, (1, 1), None])
    def test_invalid_args(n):
        """Test for invalid input args."""
        with pytest.raises(TypeError):
            max_m(n)


if __name__ == '__main__':
    unittest.main()
