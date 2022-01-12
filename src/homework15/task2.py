'''
Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors
'''


class TooManyErrors(Exception):
    '''TooManyErrors Class'''

    def __str__(self):
        return 'TooManyErrors'


def dec(fun, num_calls=2):
    """Если превышено количество попыток {num_calls}, должно быть возбуждено исключение типа

    TooManyErrors
    """

    def wrapper(*args, **kwargs):
        nonlocal num_calls
        while num_calls > 0:
            try:
                result = fun(*args, **kwargs)
                return result
            except ValueError:
                num_calls -= 1
        if num_calls == 0:
            raise TooManyErrors
    return wrapper


@dec
def func_polindrome(num: int):
    """Определяет, является ли число палиндромом (читается слева направо и справа налево одинаково).

    Число положительное целое, произвольной длины.
    """

    old_num = num
    new_num = 0

    while old_num > 0:
        new_num = new_num * 10 + old_num % 10
        old_num = old_num // 10
    if num == new_num:
        print('It is polindrome')
    else:
        print('It is not polindrome')
        raise ValueError
    return


def main():
    func_polindrome(123321)
    func_polindrome(123)
    func_polindrome(1111)


if __name__ == '__main__':
    main()
