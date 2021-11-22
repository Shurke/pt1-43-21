"""
    Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner. (все станет проще когда мы изучим
    модули, getattr и setattr)

        a. runner() – все фукнции вызываются по очереди
        b. runner(‘func_name’) – вызывается только функцию func_name.
        c. runner(‘func’, ‘func1’...) - вызывает все переданные функции

    Homework5
"""


def task5_1():
    """Генератор словаря."""
    my_dict = {my_key: my_key ** 3 for my_key in range(1, 21)}
    print('Полученный словарь: ', my_dict)
    return


def task5_2():
    """Страны и города."""
    number_country = int(input('Введите количество стран: '))
    geogr_dict = {}
    for i in range(number_country):
        country_list = list(input('Введите страну и ее города через пробел: ').split())
        geogr_dict[country_list[0]] = country_list[1:]
    number_request = int(input('Введите количество запрашиваемых городов: '))
    country_list = []
    print('Введите города через ввод: ')
    for i in range(number_request):
        city_input = input()
        for country, city in geogr_dict.items():
            if city_input in city:
                country_list.append(country)
    print('Страны, в которых находятся введенные города: ')
    print(*country_list, sep='\n')
    return


def task5_3():
    """Различные элементы в двух списках."""
    print('Введите первый список чисел через пробел: ')
    set_number_1 = (set(int(x) for x in input().split()))
    print('Введите второй список чисел через пробел: ')
    set_number_2 = (set(int(x) for x in input().split()))
    print('Количество различных чисел в обоих списках: ', end='')
    print(len(set_number_1 ^ set_number_2))
    return


def task5_4():
    """Различные элементы в одном списке."""
    print('Введите первый список чисел через пробел: ')
    set_number_1 = (set(int(x) for x in input().split()))
    print('Введите второй список чисел через пробел: ')
    set_number_2 = (set(int(x) for x in input().split()))
    print('Количество различных чисел в первом списке: ', end='')
    print(len(set_number_1 - set_number_2))
    return


def task5_5():
    """Школьники и языки."""
    number_student = int(input('Количество школьников: '))
    language_dict = {}
    for i in range(number_student):
        language_list = []
        number_language = int(input('Введите количество языков школьника: '))
        for j in range(number_language):
            language_list.append(input('Введите язык: '))
        language_dict[i] = language_list
        # Получение словаря, где ключи - номера школьников.
        # Значения словаря - списки (list) языков школьников.
    all_language = set(language_dict.get(0))  # Задать начальное значение
    least_one_language = set()
    for i in range(len(language_dict.values())):
        all_language = all_language & set(language_dict.get(i))
        least_one_language = least_one_language | set(language_dict.get(i))
    print('Количество языков, которые знают все школьники: ', len(all_language))
    print(*all_language, sep='\n')
    print('Количество языков, которые знает хотя бы один школьник: ', end='')
    print(len(least_one_language))
    # [print(i) for i in least_one_language]
    print(*least_one_language, sep='\n')
    return


def task5_6():
    """Различные слова в тексте"""
    my_string = input('Введите строку: ')
    my_set = set(my_string.split())
    print('Количество различных слов в строке: ', len(my_set))
    return


def task5_7():
    """НОД по алгоритму евклида"""
    my_int1 = int(input('Введите первое число: '))
    my_int2 = int(input('Введите второе число: '))
    if my_int1 == my_int2:
        print("Наибольший общий делитель: ", my_int2)
    else:
        while my_int1 != 0 and my_int2 != 0:
            if my_int1 > my_int2:
                my_int1 %= my_int2
            else:
                my_int2 %= my_int1
        if my_int1 == 0:
            print('Наибольший общий делитель: ', my_int2)
        else:
            print('Наибольший общий делитель: ', my_int1)
    return


def func_select(func_list_attr):
    """Интерфейс выбора доступных функций."""
    print('Доступные функции:')
    for item in range(len(func_list_attr)):
        print(func_list_attr[item], globals()[func_list_attr[item]].__doc__)
    print('Выберите через запятую '
          'название(я) функции для запуска или нажмите Enter для запуска всех функций')
    input_str = [item for item in input().split(',')]
    return input_str


def runner(*args):
    """Вызов функций"""
    if len(args) == 0:
        # Запуск всех доступных функций
        [globals()[item]() for item in func_list]
    else:
        # Запуск выбранного списка функций
        [globals()[args[0][item]]() for item in range(len(args[0]))]


# Получение списка пользовательских функций в модуле
attr_list = dir()
# Выбор доступных функций
func_list = [item for item in attr_list if not item.startswith('__') and 'task' in item]
input_func_list = func_select(func_list)

if len(input_func_list) == 1 and input_func_list[0] == '':
    # Запуск всех доступных функций, если при выборе нажат Enter
    runner()
else:
    flag = False
    for item in input_func_list:
        if item not in func_list:
            print('Некорректный ввод')
            flag = True
            break
    if not flag:
        # Запуск списка доступных функций
        runner(input_func_list)
