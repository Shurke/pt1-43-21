"""
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без
исключений (но не более n раз - параметр декоратора). Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
"""


import sys


class TooManyErrors(Exception):
    """
    Class for create Exception 'TooManyErrors'
    """

    def __str__(self):
        return 'TooManyErrors!'


def decorator_that_call_func_without_except(num_of_call: int = None):
    """The decorator accepts as input the max number of function calls

    :param num_of_call:

    :return: in case of incorrect operation of the function, the decorator throws an 'Error'

    exception;
    
    if the function has completed without exception, the decorator done its work.
    """
    if num_of_call is None:
        num_of_call = int(input('Enter nums of decorator calls: '))

    def dec(func):
        flag = True

        def wrapper(*args, **kwargs):
            nonlocal num_of_call
            nonlocal flag
            if not flag:
                print(5 * '*', 'Decorator finished work!', 5 * '*')
                sys.exit()
            if num_of_call == 0:
                raise TooManyErrors
            try:
                result = func(*args, **kwargs)
                flag = False
                return result
            except (TypeError, ZeroDivisionError):
                num_of_call -= 1
                return 'Error!'

        return wrapper

    return dec


@decorator_that_call_func_without_except()
def some_func(num):
    """Something function"""
    return 1 / num


# print(some_func(0))
# print(some_func(1))
# print(some_func(1))
