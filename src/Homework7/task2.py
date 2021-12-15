"""
Создайте декоратор, который хранит результаты вызовов
функции (за все время вызовов, не только текущий запуск программы).
"""


import datetime


def my_decorated_function(func_decorate):
    """Подсчет количества запусков функции с записью в файл CallsNumb.txt."""
    def my_wrapper(arg1):
        """Выполнение основной функции и запись в файл."""

        # Проверка наличия файла
        try:
            with open('CallsNumb.txt', 'r'):
                pass
        except FileNotFoundError:
            print('В папке с программой "task2.py" будет создан файл CallsNumb.txt')

        # Запуск основной функции
        func_result = func_decorate(arg1)

        with open('CallsNumb.txt', 'a') as my_file_write:
            now = datetime.datetime.now()
            my_file_write.write(str(now.strftime('%d-%m-%Y %H:%M')) + ' ' + str(func_result) + '\n')
    return my_wrapper


@my_decorated_function
def sq_circle(radius):
    """Определение площади круга."""
    square = 3.14 * radius ** 2
    print('Площадь круга: ', square)
    return square


print('Определение площади круга')
sq_circle(int(input('Введите радиус круга: ')))
