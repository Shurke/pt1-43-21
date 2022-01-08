"""Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится
без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors"""


class TooManyErrors(Exception):
    __module__ = Exception.__module__


def func(int1):
    int1_2 = int1

    def wrapper():
        nonlocal int1_2
        try:
            while int1_2 >= 1:
                print(int1_2)
                int1_2 = int1_2 - 1
        finally:
            raise TooManyErrors

    return wrapper()


@func(4)
def a():
    return


a()
