"""
Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без
исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
"""


class TooManyErrors(Exception):
    """rises exception if number of attempts > param"""


def param_decorator(number_of_calls: int) -> callable:
    """param decorator function that decorates another function and
    calls it until it is called with exceptions, but no more than
    param - 'number_of_calls' times
    :param number_of_calls: gets number of available function calls"""
    def decorator(given_function: callable) -> callable:
        def wrapper(*args: int) -> None:
            nonlocal number_of_calls
            number_of_calls -= 1
            try:
                print(given_function(*args))
                exit(0)
            except TypeError:
                print(f'Wrong type of given data!\n{number_of_calls} attempts left!')
            if number_of_calls == 0:
                raise TooManyErrors('You have exceed the amount of attempts!')
        return wrapper
    return decorator


@param_decorator(int(input('Enter decorator param: ')))
def pow_of_two_numbers(x: int, y: int) -> str:
    """returns x pow y"""

    return f'{x} pow {y} is - {x ** y}'


def main():
    pow_of_two_numbers(2, 't')
    pow_of_two_numbers(2, 'r')
    pow_of_two_numbers(2, 'y')
    pow_of_two_numbers(2, 'u')
    pow_of_two_numbers(2, 3)


if __name__ == '__main__':
    main()
