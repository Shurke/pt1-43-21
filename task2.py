"""Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится
без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors"""


class TooManyErrors:
    pass


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


func(int(input("введите число раз вызова функции: ")))
