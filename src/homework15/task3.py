"""Задача 3, Вариант 4.

Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами.
Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится
‘assertRaises’. Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама.
"""


"""Вы помещаете свои тесты в методы класса unittest.TestCase
Вы используете ряд специальных методов утверждения класса unittest.TestCase вместо встроенного оператора assert"""

"""Method	Equivalent to
.assertEqual(a, b)	a == b
.assertTrue(x)	bool(x) is True
.assertFalse(x)	bool(x) is False
.assertIs(a, b)	a is b
.assertIsNone(x)	x is None
.assertIn(a, b)	a in b
.assertIsInstance(a, b)	isinstance(a, b)"""

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
if __name__ == "__main__":
    test_sum()
    print("Everything passed")



import unittest
class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
if __name__ == '__main__':
    unittest.main()

import unittest
from my_sum import sum
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main()