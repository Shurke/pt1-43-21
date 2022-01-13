'''Tests for task4'''

import pytest
from task4 import *


class TestGreatCommDivisor:

    @pytest.mark.parametrize("a, b, result", [(10, 20, 10),
                                            (144, 136, 8),
                                            (123, 1246, 1),
                                            (-9, 8, 1),
                                            (8, -9, 1)])
    def test_great(self, a, b, result):
        '''positive tests for GCD'''

        assert great_comm_divisor(a, b) == result
        with pytest.raises(TypeError):
            great_comm_divisor('a', 'b')

    @pytest.mark.parametrize("a, result", [(15, [1, 2, 4, 7, 8, 11, 13, 14])])
    def test_mutually_simple_list(self, a, result):
        '''positive tests for mutually_simple_list'''

        assert mutually_simple_list(a) == result
        with pytest.raises(TypeError):
            mutually_simple_list('str')

    @pytest.mark.parametrize('n', ['a', {'a': 3}, (1, 1), None])
    def test_invalid_args(self, n):
        """Test for invalid input args."""

        with pytest.raises(TypeError):
            max_m(n)

    @pytest.mark.parametrize("a, b, result", [([1, 2, 4, 7, 8, 11, 13, 14], 15, [1, 4, 11])])
    def test_modulo_inverse_list(self, a, b, result):
        '''positive tests for modulo_inverse_list'''

        assert modulo_inverse_list(a, b) == result
        with pytest.raises(TypeError):
            modulo_inverse_list(1)

    @pytest.mark.parametrize('n, result', [(15, 11), (100, 51), (7, 1)])
    def test_max_m(self, n, result):
        '''positive tests for max_m function'''

        assert max_m(n) == result
        with pytest.raises(TypeError):
            max_m('a')

    @pytest.mark.parametrize('lst, result', [([7, 15, 100], 63)])
    def test_sum_func(self, lst, result):
        '''positive test for sum_function'''

        assert sum_func(lst) == result
