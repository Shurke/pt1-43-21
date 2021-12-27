"""
Тесты задачи task_4.

Задача Эйлера №452
Определим F(m,n) как количество кортежей положительных чисел длиной n,
произведение всех элементов которых не превышает m.

F(10, 10) = 571.

F(106, 106) mod 1 234 567 891 = 252903833.

Найдите F(10**9, 10**9) mod 1 234 567 891.

Расчет задачи занимает много времени.
"""

import pytest
import task4


def test_one_right_main():
    """Тест №1 на правильность выполнения main."""
    t_problem = task4.Problem(11111, 10, 1)
    t_expected = 571
    assert t_problem.solve() == t_expected


def test_two_right_main():
    """Тест №2 на правильность выполнения main."""
    t_problem = task4.Problem(1234567891, 10**6, 1000)
    t_expected = 252903833
    assert t_problem.solve() == t_expected


def test_three_wrong_main():
    """Негативный тест №3 на правильность выполнения main (правильный ответ - 2954)."""
    t_problem = task4.Problem(11111, 20, 1)
    t_expected = 2900
    assert t_problem.solve() != t_expected


def test_four_right_getprimes():
    """Тестирование функции get.

    Тестирование функции get класса Prime - создание списка
    простых чисел в заданном диапазоне n.

    """
    t_get_prime = task4.Prime
    t_expected = [2, 3, 5, 7, 11, 13, 17, 19]
    assert t_get_prime.get(20) == t_expected


def test_five_wrong_getprimes():
    """Негативный тест функции get.

    Негативный тест функции get класса Prime - создание списка
    простых чисел в заданном диапазоне.

    """
    t_get_prime = task4.Prime
    t_expected = [2, 3, 5, 7, 11, 13, 17, 18, 19]
    assert t_get_prime.get(20) != t_expected


def test_six_wrong_n_getprimes():
    """Негативный тест функции get класса Prime: n - нецелое число."""
    t_get_prime = task4.Prime
    with pytest.raises(TypeError):
        t_get_prime.get(20.4)


def test_seven_out_type_getprimes():
    """Проверка типа результата выполнения функции get класса Prime."""
    t_get_prime = task4.Prime
    assert isinstance(t_get_prime.get(10), list)


def test_eight_right_getbinom():
    """Тестирование функции get.

    Тестирование функции get класса BinomialCoefficient - расчет
    биномиальных коэффициентов m по n.

    """
    t_get_binom = task4.BinomialCoefficient(111111)
    t_expected = 10
    assert t_get_binom.get(5, 3) == t_expected


def test_nine_wrong_mod_getproblem():
    """Негативный тест функции get.

     Негативный тест функции get класса Problem: количество блоков
     не соответствует заданному числу.

     """
    t_get_problem = task4.Problem(1111, 10, 3)
    with pytest.raises(AssertionError):
        t_get_problem.get(10, 3)
