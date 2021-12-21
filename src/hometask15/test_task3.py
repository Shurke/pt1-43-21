"""
Testing module for 'task3.py'
tests function 'get_ranges'
tests function 'add_to_ans_list'
"""


import unittest
from ddt import data
from ddt import ddt
from ddt import unpack
from task3 import get_ranges, add_to_ans_list, LengthError, ArgumentsError


@ddt
class TestGetRanges(unittest.TestCase):
    @data(
        ([0, 1, 2, 3, 4, 7, 8, 10], '0-4,7-8,10'),
        ([4, 7, 10], '4,7,10'),
        ([2, 3, 8, 9], '2-3,8-9'),
        ([1, 2, 3, 4, 6, 8, 10, 11, 12, 15], '1-4,6,8,10-12,15')
    )
    @unpack
    def test_validate_case(self, input_list, expected):
        self.assertEqual(get_ranges(input_list), expected)

    @data([])
    def test_bad_cases(self, input_list):
        print(len(input_list))
        self.assertRaises(LengthError, get_ranges, input_list)

    @data(
        [1, 'a', 3, 6],
        's',
        [1.5, 2.0, 3.0, 5.0, 6.0],
        0,
        '1, 2, 3, 4, 5'
    )
    def test_bad_case(self, input_list):
        self.assertRaises(ValueError, get_ranges, input_list)


@ddt
class TestAddAnsToList(unittest.TestCase):
    @data(
        (5, 6, ['1-3', '4'], ['1-3', '4', '5-6']),
        (1, 7, [], ['1-7']),
        (11, 11, ['1-4', '6', '7', '8-9'],
         ['1-4', '6', '7', '8-9', '11'])
    )
    @unpack
    def test_valid_cases(self, start, end, ans_list, expected):
        add_to_ans_list(ans_list, start, end)
        self.assertEqual(ans_list, expected)

    @data(
        (('1-3', '5-6', '7'), 8, 9),
        (('1-3', '5', '6-9'), 'd', 9),
        (('1-2', '4-9', '10'), 11, 's'),
        (('1-4', '5-8', '11'), 9, 8),
    )
    @unpack
    def test_wrong_arguments(self, *args):
        self.assertRaises(ArgumentsError, add_to_ans_list, *args)


if __name__ == '__main__':
    unittest.main()
