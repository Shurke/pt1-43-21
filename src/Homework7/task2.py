"""
Создайте декоратор, который хранит результаты вызовов
функции (за все время вызовов, не только текущий запуск программы).
"""


def my_decorated_function(func_decorate):
    """Подсчет количества запусков модуля с записью в файл CallsNumb.txt."""
    def my_wrapper(arg1):
        """Работа с файлом и выполнение основной функции."""
        # Проверка наличия файла
        try:
            my_file_read = open('CallsNumb.txt', 'r')
            call_number = int(my_file_read.read().rstrip())
            my_file_read.close()
        except FileNotFoundError:
            call_number = 0

        # Запуск основной функции
        func_decorate(arg1)

        call_number += 1

        with open('CallsNumb.txt', 'w') as my_file_write:
            my_file_write.write(str(call_number))
        print('Количество запусков программы: ', call_number)
    return my_wrapper


@my_decorated_function
def sq_circle(radius):
    """Определение площади круга."""
    square = 3.14 * radius ** 2
    print('Площадь круга: ', square)
    return


print('Определение площади круга')
sq_circle(int(input('Введите радиус круга: ')))
