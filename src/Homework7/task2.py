"""
Создайте декоратор, который хранит результаты вызовов
функции (за все время вызовов, не только текущий запуск программы)
"""


def my_decorated_function(func_decorate):
    """Подсчет количества запусков модуля с записью в файл CallsNumb.txt"""
    def my_wrapper(arg1):
        """Работа с файлом и выполнение основной функции"""
        # Проверка наличия файла
        try:
            my_file_read = open('CallsNumb.txt', 'r')
        except FileNotFoundError:
            my_file_read = open('CallsNumb.txt', 'w+')
        call_number_str = my_file_read.read().rstrip()

        # Проверка наличия записи в файле
        if call_number_str == '':
            call_number = 0
        else:
            call_number = int(call_number_str)
        my_file_read.close()
        # Запуск основной функции
        func_decorate(arg1)
        my_file_write = open('CallsNumb.txt', 'w')
        my_file_write.write(str(call_number + 1))
        my_file_write.close()
        print('Количество запусков программы: ', call_number + 1)
    return my_wrapper


@my_decorated_function
def sq_circle(radius):
    """Определение площади круга"""
    square = 3.14 * radius ** 2
    print('Площадь круга: ', square)
    return


print('Определение площади круга')
sq_circle(int(input('Введите радиус круга: ')))
