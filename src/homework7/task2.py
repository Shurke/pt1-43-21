'''
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''

import datetime


def dec(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        dat = str(datetime.datetime.now())
        with open("task2_mem.txt", "a") as f:
            f.writelines(dat + ' | ' + str(result) + '\n')
        return result
    return wrapper


@dec
def func(a, b):
    return a + b


print(func(1, 2))
print(func(3, 4))
print(func(5, 6))
