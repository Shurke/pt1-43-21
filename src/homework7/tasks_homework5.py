def task1_5():
    """Задача 1, Dict comprehensions

    Создайте словарь с помощью генератора словарей, так чтобы его ключами
    были числа от 1 до 20, а значениями кубы этих чисел.

    """

    dict1 = {x: x ** 3 for x in range(1, 21)}
    for key, item in dict1.items():
        print(key, ":", item)


def task2_5():
    """Задача2, Города

    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.
    Входные данные
    Программа получает на вход количество стран N.
    Далее идет N строк, каждая строка начинается с названия страны,
    затем идут названия городов этой страны. В следующей строке записано
    число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
    Выходные данные
    Для каждого из запроса выведите название страны, в котором находится данный город.
    Примеры
    Входные данные
    2
    Russia Moscow Petersburg Novgorod Kaluga
    Ukraine Kiev Donetsk Odessa
    3
    Odessa
    Moscow
    Novgorod
    Выходные данные
    Ukraine
    Russia
    Russia

    """
    dict_city_country_g = __get_input_dictionary_city_country()
    if dict_city_country_g:
        __find_country(dict_city_country_g)


def __get_input_dictionary_city_country():
    """функция возвращает словарь городов и стран"""
    try:
        quantity_of_countries = int(input("Введите количество стран: "))
    except ValueError:
        print("Это не число")
        return
    dict_city_country = dict()
    for i in range(quantity_of_countries):
        country_and_cities = input("Введите страну и ее города: ")
        list_country_and_cities = country_and_cities.split()
        if len(list_country_and_cities) < 1:
            continue
        country = list_country_and_cities[0]
        for city in list_country_and_cities[1:]:
            dict_city_country[city] = country
    return dict_city_country


def __find_country(dict_city_country):
    """функция возвращает страну по городу"""
    try:
        quantity_of_cities = int(input("Введите количество городов: "))
    except ValueError:
        print("Это не число")
        return
    list_of_cities = list()
    for i in range(quantity_of_cities):
        list_of_cities.append(input("Введите города: "))
    for city in list_of_cities:
        print(dict_city_country.get(city))


def task3_5():
    """Задача 3.

    Даны два списка чисел. Посчитайте, сколько различных чисел содержится
    одновременно как в первом списке, так и во втором.

    """

    list1 = input("Введите первый список чисел: ").split()
    list2 = input("Введите второй список чисел: ").split()
    set1 = set(list1)
    set2 = set(list2)
    print((
        "Одновременно как в первом списке, так и во втором списке "
        f"содержится различных чисел: {len(set1 & set2)} ."
    ))


def task4_5():
    """Задача 4.

    Даны два списка чисел. Посчитайте, сколько различных чисел
    входит только в один из этих списков

    """

    list1 = input("Введите первый список чисел: ").split()
    list2 = input("Введите второй список чисел: ").split()
    set1 = set(list1)
    set2 = set(list2)
    print(f"{len(set1 ^ set2)} различных чисел входит только в один из списков")


def task5_5():
    """Задача 5. Языки

    Каждый из N школьников некоторой школы знает Mi языков. Определите,
    какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
    Входные данные
    Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
    после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
    Пример входных данных:
    3          # N количество школьников
    2          # M1 количество языков первого школьника
    Russian    # языки первого школьника
    English
    3          # M2 количество языков второго школьника
    Russian
    Belarusian
    English
    3
    Russian
    Italian
    French
    Выходные данные
    В первой строке выведите количество языков, которые знают все школьники.
    Начиная со второй строки - список таких языков.
    Затем - количество языков, которые знает хотя бы один школьник,
    на следующих строках - список таких языков.
    """
    __get_languages()


def __get_languages():
    """функция возвращает языки, которые знают школьники"""
    try:
        quantity_of_schoolchildren = int(input("Введите количество школьников: "))
    except ValueError:
        print("Это не число")
        return
    list_of_schoolchildren = list()
    for i in range(quantity_of_schoolchildren):
        try:
            quantity_of_languages = int(input("Введите количество языков,"
                                              " которые знает школьник: "))
        except ValueError:
            print("Это не число")
            return
        set_i = set()
        for j in range(quantity_of_languages):
            set_i.add(input("Введите язык: "))
        list_of_schoolchildren.append(set_i)
    known_by_everybody = set.intersection(*list_of_schoolchildren)
    known_by_somebody = set.union(*list_of_schoolchildren)
    print(f"языки, котрые знают все школьники: {len(known_by_everybody)}",
          *known_by_everybody, sep="\n")
    print(f"языки, котрые знает хотя бы один школьник: {len(known_by_somebody)}",
          *known_by_somebody, sep="\n")


def task6_5():
    """Задача 6. Слова

    Во входной строке записан текст. Словом считается последовательность
    непробельных символов идущих подряд, слова разделены одним или большим
    числом пробелов или символами конца строки. Определите, сколько различных
    слов содержится в этом тексте.

    """

    user_text = input("Введите текст: ")
    our_set = set(user_text.split())
    print(len(our_set))


def task7_5():
    """Задача 7. Оглянемся назад. Числа

    Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
    алгоритма Евклида (мы не знаем функции и рекурсию).

    """
    try:
        number1 = int(input("Введите первое число: "))
        number2 = int(input("Введите вторе число: "))
    except ValueError:
        exit(print("Это не число"))

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1

    print("Наибольший общий делитель:", max(number1, number2))
