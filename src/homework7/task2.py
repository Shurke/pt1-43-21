'''
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''


def dec(fun):
    num = 0

    def wrapper(*args, **kwargs):
        nonlocal num
        print('Call num:')
        num += fun()
        return num
    return wrapper


@dec
def func():
    return 1


print(func())
print(func())
print(func())
