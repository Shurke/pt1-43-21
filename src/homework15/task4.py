'''
Проект Эйлера.
Задача 69/Максимум функции Эйлера
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества чисел,
меньших n, которые взаимно просты с n.
К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9)=6.
Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.
'''

import unittest


def euler_task_69(n):
    """Totient maximum. Problem 69"""
    max_val = 0
    max_totient = 0
    totient = [i for i in range( n + 1)]
    for item in range(2, n + 1):
        if totient[item] == item:
            for item2 in range(item, n + 1, item):
                totient[item2] -= totient[item2] // item
        val = item / totient[item]
        if max_val < val:
            max_val = val
            max_totient = item
    print("Max value:", max_totient)
    return max_totient


class TestTask(unittest.TestCase):

    def test_type(self):
        """Test for function input type"""
        self.assertRaises(TypeError, euler_task_69, 2132131)
        self.assertRaises(TypeError, euler_task_69, 1.23)

    def test_result(self):
        """Test for result equality"""
        self.assertEqual(euler_task_69(1000000), 510510)
        self.assertEqual(euler_task_69(1000000), 1)
        self.assertEqual(euler_task_69(1000), 12312)


if __name__ == '__main__':
    unittest.main()
