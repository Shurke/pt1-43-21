"""
Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors
"""


class TooManyErrors(ValueError):
    pass


def dec(func):
    def wrapper(num_rep):
        counter = 0
        while counter < num_rep:
            try:
                result = func(num_rep)
                return result
            except ValueError:
                counter += 1
        raise TooManyErrors("Превышено количество попыток!")
    return wrapper


@dec
def my_func(num):
    numeral = int(input(f"Всего попыток: {num}\nВведите цифру: "))
    print(f"Вот такое число введено: {numeral}")


my_num = int(input("Введите лимит для выполнения декоратора (условие): "))
my_func(my_num)
