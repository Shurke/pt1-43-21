"""
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без
исключений (но не более n раз - параметр декоратора). Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
"""

import sys


def decorator_that_call_func_without_except(num_of_call: int):
    """
    The decorator accepts as input the max number of function calls
    :param num_of_call:
    :return: in case of incorrect operation of the function, the decorator throws an 'Error' exception;
    if the function has completed without exception, the decorator done its work.
    """
    def dec(func, flag=True):
        def wrapper(*args, **kwargs):
            nonlocal num_of_call
            nonlocal flag
            if not flag:
                sys.exit(1)
            if num_of_call == 0:
                raise 'TooManyErrors'
            try:
                result = func(*args, **kwargs)
                flag = False
                return result
            except:
                num_of_call -= 1
                return 'Error!'

        return wrapper

    return dec


@decorator_that_call_func_without_except(int(input('Enter nums of decorator calls: ')))
def some_func(a):
    return 1 / a


print(some_func(0))
print(some_func(1))
print(some_func(0))
