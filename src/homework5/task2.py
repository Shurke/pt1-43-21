'''Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''


from datetime import datetime
from math import pi


def remember_everything(area_of_circle):
    def wrapper(args):
        result = area_of_circle(args)
        date = str(datetime.now().time())[:-7]
        with open('Decorator counter.txt', 'a') as f:
            f.write(f'{date} r = {str(args)} , S = {str(result)}, \n')
        return result
    return wrapper

@remember_everything
def area_of_circle(r):
    return round(pi, 5) * r ** 2

print(area_of_circle(2))
print(area_of_circle(3))
print(area_of_circle(1))
