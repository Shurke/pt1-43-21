"""Создайте декоратор, который хранит результаты вызовов функции (за
все время вызовов, не только текущий запуск программы)"""


def dec(func_s):

    def wrapper(*args, **kwargs):
        res = func_s(*args, **kwargs)
        with open('save.txt', 'a') as fh:
            fh.write(f"{res}\n")
        return res
    return wrapper


@dec
def func_s(a, b):
    return a + b


func_s(1, 1)
func_s(1, 2)
func_s(1, 3)
