"""
Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами.
Учтите, что в функцию могут быть переданы некорректные значения,
здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама.
"""

import unittest


def task_func(input_str):
    """4.Пары элементов

    Дан список чисел.Посчитайте, сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента, равные друг другу образуют одну пару,
    которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    """
    cnt = 0
    lst = input_str.split()

    for ind1 in range(len(lst) - 1):
        l2_start_ind = ind1 + 1
        for ind2 in range(l2_start_ind, len(lst)):
            if lst[ind1] == lst[ind2]:
                cnt += 1
    print('Pairs num:', cnt)
    return cnt


class TestTask(unittest.TestCase):

    def test_type(self):
        """Test for function input type"""
        self.assertRaises(TypeError, task_func, 2132131)
        self.assertRaises(TypeError, task_func, 99.9293123)
        self.assertRaises(TypeError, task_func, False)
        self.assertRaises(TypeError, task_func, (123, 3213, 1231231))

    def test_result(self):
        """Test for result equality"""
        self.assertEqual(task_func("1 1 1"), 2)
        self.assertEqual(task_func("1 1 1 1"), 6)


if __name__ == '__main__':
    unittest.main()
