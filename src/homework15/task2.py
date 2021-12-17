""" Задача 2.

Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors

"""


class TooManyErrors(Exception):
    def __init__(self, text):
        self.txt = text


def param_dec(max_number_of_calls, number_of_calls=1):

    def call_function(func):

        def wrapper(*args, **kwargs):
            nonlocal number_of_calls
            nonlocal max_number_of_calls
            while number_of_calls <= max_number_of_calls:
                print("Попытка №: ", number_of_calls)
                try:
                    func(*args, **kwargs)
                    break
                except:
                    number_of_calls += 1
            if number_of_calls > max_number_of_calls:
                raise TooManyErrors("Функция была вызвана слишком много раз")

        return wrapper

    return call_function


@param_dec(5)
def our_function():
    number = input("Введите число: ")
    number = int(number)
    print("Функуия выполнилась успешно")


our_function()
