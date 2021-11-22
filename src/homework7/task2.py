'''
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''

import datetime


def dec(fun):
    def wrapper(*args, **kwargs):
        dat = str(datetime.datetime.now())
        tmp_file = open("task2_mem.txt", "a")
        result = fun(*args, **kwargs)
        tmp_file.writelines(dat + ' | ' + str(result) + '\n')
        tmp_file.close()
        return result
    return wrapper


@dec
def func(a, b):
  return a + b


print(func(1, 2))
print(func(3, 4))
print(func(5, 6))
