"""
2.	Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
Задачу поместите в файл task2.py в папке src/homework7.
"""


def memory(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        f = open('task2results.txt', 'a')
        f.write(str(result) + '\n')
        f.close()
        return result

    return wrapper


@memory
def func(a, b):
    return a + b


print(func(1, 1))
print(func(1, 2))
print(func(1, 3))
