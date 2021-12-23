"""
Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors
"""


class TooManyErrors(ValueError):
    pass


def dec(num_rep):
    def execution(func):
        def wrapper():
            nonlocal num_rep
            counter = 0
            while counter < num_rep:
                try:
                    result = func()
                    return result
                except ValueError:
                    counter += 1
            raise TooManyErrors("Превышено количество попыток!")
        return wrapper
    return execution


my_num = int(input("Введите лимит для выполнения декоратора (условие): "))


@dec(my_num)
def my_func():
    calls = my_num
    numeral = int(input(f"Всего попыток: {calls}\nВведите цифру: "))
    calls -= 1
    print(f"Вот такое число введено: {numeral}")


my_func()
