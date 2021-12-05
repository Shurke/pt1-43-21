"""
Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов,
не только текущий запуск программы)
"""


import datetime


def save_res(func):
    """Decorator create file that contain date, counts and result of function  call"""
    counter = 1

    def wrapper(*args, **kwargs):
        nonlocal counter
        date = str(datetime.datetime.today())[:-7]
        result = func(*args, **kwargs)
        with open(date, 'a') as fh:
            fh.write(f'{date}: function called {counter} times. Result: {result}.\n')
        counter += 1
        return result
    return wrapper


@save_res
def sum_(a: int, b: int) -> int:
    return a + b


print(sum_(1, 2))
print(sum_(2, 3))
print(sum_(2, 3))
print(sum_(2, 3))
print(sum_(27, 3))
print(sum_(2, 3))
