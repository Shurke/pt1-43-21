""" Задача 2.

Создайте декоратор, который хранит результаты вызовов функции (за все время
вызовов, не только текущий запуск программы)
Задачу поместите в файл task2.py в папке src/homework7.
"""
from datetime import datetime


def total_recall(my_func):

    def wrapper(*args):

        result = my_func(*args)
        line = " " + str(datetime.now().time()) + " аргументы: " + str(args)
        line = line + " результат: " + str(result) + '\n'
        with open("recollection.txt", "a") as f:
            f.write(line)

        return result

    return wrapper


@total_recall
def my_func(a, b):
    return a + b


print(my_func(1, 1))
print(my_func(1, 1))
print(my_func(1, 3))
print(my_func(1, 2))
print(my_func(1, 1))
