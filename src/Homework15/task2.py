"""
Декоратор с повторным вызовом.

Создайте декоратор, который вызывает задекорированную функцию,
пока она не выполнится без исключений (но не более n раз - параметр
декоратора). Если превышено количество попыток, должно быть
возбуждено исключение типа TooManyErrors.
"""


class TooManyErrors(Exception):
    """Вызов пользователького исключения."""
    def __init__(self, *args):
        if args:
            self.descr = args[0]
        else:
            self.descr = None

    def __str__(self):
        if self.descr:
            return 'TooManyErrors, {0} '.format(self.descr)
        else:
            return 'TooManyErrors'


def repeat_decorator(num):
    """Декоратор с параметром."""
    def decor(func_to_decorate):
        def wrapper():
            nonlocal num
            while num > 0:
                try:
                    func_to_decorate()
                    break
                except ValueError:
                    num -= 1
                    print('Ошибка ввода!')
            if num == 0:
                raise TooManyErrors('Превышен лимит ошибок ввода!')
        return wrapper
    return decor


num_repeat = int(input('Введите количество попыток ввода числа: '))


@repeat_decorator(num_repeat)
def function_befor_decoration():
    """Вычисление квадратного корня."""
    val_item = int(input('Введите целое положительное число: '))
    if val_item >= 0:
        out_item = val_item ** (1 / 2)
        print('Квадратный корень из', val_item, 'равен', '{:.2f}'.format(out_item))
    else:
        raise ValueError


function_befor_decoration()
