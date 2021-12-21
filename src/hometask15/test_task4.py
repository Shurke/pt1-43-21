"""
Testing module for 'task4.py';
tests function 'max_product'
tests function 'converting_to_list'
"""

from ddt import data
from ddt import ddt
from ddt import unpack
from task4 import converting_to_list
from task4 import max_product
import unittest


@ddt
class TestMaxProductFunction(unittest.TestCase):
    """testing Max Product function"""

    @data(
        ('1234567890', 2, 72),
        ('109034567910', 2, 63),
        ('9017539683', 3, 432),
    )
    @unpack
    def test_normal_case(self, num1, multipliers, expected):
        self.assertEqual(expected, max_product(num1, multipliers))

    @data(
        (('df', 23), 'f'),
        ([1, 2, 3, 4], '5'),
        (1234.456, 4),
        ((1, 2, 3, 4), 1)
    )
    @unpack
    def test_wrong_input_data(self, *args):
        self.assertRaises(ValueError, max_product, *args)

    @data(
        ([1, 2, 3, 4], 0),
        ([1, 6, 9, 4, 7, 0], -1),
        ([6, 1, 9, 9, 8], -100)
    )
    @unpack
    def test_negative_multiplier(self, *args):
        self.assertRaises(ValueError, max_product, *args)

    @data(("""73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""", 13, 23514624000))
    @unpack
    def test_euler_project(self, num1, multipliers, expected):
        self.assertEqual(expected, max_product(num1, multipliers))


@ddt
class TestConvertingToList(unittest.TestCase):
    """testing function converting_to_list"""

    @data(
        ('123456', [1, 2, 3, 4, 5, 6]),
        ('145078', [1, 4, 5, 0, 7, 8]),
        ('1269804', [1, 2, 6, 9, 8, 0, 4])
    )
    @unpack
    def test_validate_cases(self, input_str, expected):
        self.assertEqual(expected, converting_to_list(input_str))

    @data('123456 67657',
          '32489234g4324',
          '-324=818394',
          '0039!/32')
    def test_bad_cases(self, *args):
        self.assertRaises(ValueError, converting_to_list, *args)


if __name__ == '__main__':
    unittest.main()
