"""Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов,
не только текущий запуск программы)
"""


import os


def dec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if os.path.exists('statistic.txt'):
            with open('statistic', 'w') as f:
                digit = f.read().split("\n")
                digit = int(digit[0])
                f.close()
        else:
            digit = 0
        with open('statistic.txt', 'w') as f:
            f.write(str(digit + 1))
            f.close()
        return result
    return wrapper


@dec
def my_func():
    return 1


my_func()
