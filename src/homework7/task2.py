"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""


def dec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        file = open('/Users/mironchuduk/git/pt1-43-21/src/res', 'a')
        file.write(f'{result}\n')
        file.close()
        return result
    return wrapper


@dec
def my_func():
    return "Результат вызова функции"


print(my_func())
