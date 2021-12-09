"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""


def dec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('res', 'a') as file:
            file.write(f'{result}\n')
        return result
    return wrapper


@dec
def my_func():
    return "Результат вызова функции"


print(my_func())
