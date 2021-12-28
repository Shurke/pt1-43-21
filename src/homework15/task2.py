'''2. Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений (но не более n раз - параметр декоратора).

Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors
'''


class TooManyErrors(BaseException):
    pass


def dec_too_many_errors(num):
    '''Вызывает задекорированную функцию, пока она не выполнится без исключений.

    Если превышено кол-во попыток n - возбуждает исключение типа TooManyErrors
    '''

    def dec(fun):
        def wrapper():
            try:
                fun()
            except Exception:
                a = 0
                while a < num:
                    try:
                        fun()
                    except Exception:
                        a += 1
                        print(f"Было обработано исключение №{a}")
                        continue
                if a == num:
                    raise TooManyErrors
            else:
                return 'Function works'
        return wrapper
    return dec


@dec_too_many_errors(3)
def division_func(a: int = 10, b: int = 0) -> int:
    '''Находит целочисленное частное от деления a на b'''
    result = a / b
    return result


print(division_func())
