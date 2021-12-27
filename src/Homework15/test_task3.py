"""
Тесты задачи task_3.
"""

import pytest


def get_range(my_string):
    """Реализовать функцию get_ranges.

     Функция получает на вход непустой список неповторяющихся целых чисел,
     отсортированных по возрастанию, и “сворачивает” этот список.
     get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
     get_ranges([4,7,10]) // "4,7,10"
     get_ranges([2, 3, 8, 9]) // "2-3,8-9".

     """
    input_list = list(map(int, my_string.split(',')))
    out_str = str(input_list[0])
    for item in range(1, len(input_list)):
        # Проврка наличия последовательности
        if input_list[item] == input_list[item - 1] + 1:
            if out_str[-1] != '-':
                # Проверка повторности последовательности
                out_str = out_str + '-'
            elif out_str[-1] == '-' and item == len(input_list) - 1:
                out_str = out_str + str(input_list[item])
        else:
            if out_str[-1] != '-':
                out_str = out_str + ',' + str(input_list[item])
            else:
                out_str = out_str + str(input_list[item - 1]) + ',' + str(input_list[item])
    print('"Свернутый" список: ', out_str)
    return out_str


def test_executive_right_one():
    """Тест на правильность выполнения 1."""
    t_func = get_range('0, 1, 2, 3, 4, 7, 8, 10')
    t_expected = '0-4,7-8,10'
    assert t_func == t_expected


def test_executive_right_two():
    """Тест на правильность выполнения 2."""
    t_func = get_range('1, 3, 4, 5, 8, 9, 10, 14, 15, 16')
    t_expected = '1,3-5,8-10,14-16'
    assert t_func == t_expected


def test_executive_right_three():
    """Тест на правильность выполнения 3."""
    t_func = get_range('1, 3, 5')
    t_expected = '1,3,5'
    assert t_func == t_expected


def test_check_input_str():
    """Негативный тест: ввод содержит буквы"""
    with pytest.raises(ValueError):
        get_range('1,2,ab,3')


def test_check_input_float():
    """Негативный тест: ввод содержит число с плавающей запятой"""
    with pytest.raises(ValueError):
        get_range('1,2,10.5,3')


def test_out_type():
    """Проверка типа результата выполнения функции get_range"""
    t_func = get_range('1,2,3')
    assert isinstance(t_func, str)
