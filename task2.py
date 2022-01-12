"""Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится
без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors"""


class TooManyErrors(ValueError):
    pass


def dec(num):
    def dec2(func):
        def wrapper():
            n = 0
            while n < num:
                try:
                    result = func()
                    return result
                except ValueError:
                    n += 1
            raise TooManyErrors("Превышено количество попыток!")
        return wrapper
    return dec2


my_num = 2


@dec(my_num)
def my_func():
    a = my_num
    try:
        while a >= 1:
            print(a)
            a = a - 1
    finally:
        raise ValueError


my_func()
