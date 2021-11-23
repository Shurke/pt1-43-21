# -*- coding: utf8 -*-
"""
Создайте декоратор, который хранит результаты вызовов функции (за все время
вызовов, не только текущий запуск программы)
Задачу поместите в файл task2.py в папке src/homework7.
"""


def decorator(func):
    """
    decorator of functions, that saves cache
    of outputs
    """

    def wrapper(*args):
        result = func(*args)
        file_adder = open('task2_cache.txt', 'a')
        file_adder.write(str(result))
        file_adder.write('\n')
        file_adder.close()
        return result
    return wrapper


@decorator
def function_pow(number1, number2):
    """
    returns number1 power number2
    """

    return number1 ** number2


def main():
    function_pow(2, 7)
    function_pow(2, 8)
    function_pow(3, 9)
    function_pow(4, 10)
    cache_file = open('task2_cache.txt', 'r')
    print(cache_file.read())
    cache_file.close()


main()
