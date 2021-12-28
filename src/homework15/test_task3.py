'''Tests for task3'''

from ddt import data
from ddt import ddt
from ddt import unpack
from task3 import pair_counter_func
import unittest
from unittest.case import TestCase


@ddt
class TestPairCounterFunc(TestCase):
    '''Тесты для pair_counter_func()'''

    @data(('1 1 1 1', 6),
          ('1 1 1', 3),
          (' 1 1 1 1 2 2', 7),
          ('1 1 1 2 2 2 ', 6)
          )
    @ unpack
    def test_positive_solo_numbers(self, value, expected):
        '''Тесты, покрывают положительные одноразрядные числа'''

        self.assertEqual(pair_counter_func(value), expected)

    @data(1, None, True, [1, 2], (1, 2), {1, 2})
    def test_wrong_input(self, value):
        '''Тесты, рассчитанные на неверный тип входных данных'''

        with self.assertRaises(AttributeError):
            pair_counter_func(value)

    @data(('-1 -1', 1),
          ('-1 -1 -1', 3),
          (' -1 -1 -1 -1 -2 -2 ', 7),
          ('-1 -1 1 1 ', 2),
          )
    @unpack
    def test_negative_numbers(self, value, expected):
        '''Тесты, рассчитанные на наличие отрицательных чисел'''

        self.assertEqual(pair_counter_func(value), expected)

    @data(('1', 0),
          ('1 1 1 2', 3),
          (' 1 1 1 1 2 2 5', 7),
          ('1 1 11', 1),
          ('1 1 1 2 2 2 ', 6)
          )
    @ unpack
    def test_no_pairs_numbers(self, value, expected):
        '''Тесты, рассчитанные на наличие беспарных элементов'''

        self.assertEqual(pair_counter_func(value), expected)

    @data(('11 11', 1),
          ('1 1 11 11 11', 4),
          (' 111 111 22 22', 2)
          )
    @ unpack
    def test_more_than_one_digit_numbers(self, value, expected):
        '''Тесты, рассчитанные на числа имеющие более одного разряда'''

        self.assertEqual(pair_counter_func(value), expected)


if __name__ == '__main__':
    unittest.main()
