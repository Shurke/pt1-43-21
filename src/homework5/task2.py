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


def get_input_dictionary_city_country():
    """функция возвращает словарь городов и стран"""
    try:
        quantity_of_countries = int(input("Введите количество стран: "))
    except ValueError:
        print("Это не число")
        return
    dict1 = dict()
    for i in range(quantity_of_countries):
        country_and_cities = input("Введите страну и ее города: ")
        list_country_and_cities = country_and_cities.split()
        if len(list_country_and_cities) < 1:
            continue
        country = list_country_and_cities[0]
        for city in list_country_and_cities[1:]:
            dict1[city] = country
    return dict1


def find_country():
    """функция возвращает страну по городу"""
    try:
        quantity_of_cities = int(input("Введите количество городов: "))
    except ValueError:
        print("Это не число")
        return
    list_of_cities = list()
    for i in range(quantity_of_cities):
        list_of_cities.append(input("Введите город: "))
    for city in list_of_cities:
        print(dict_city_country.get(city))


dict_city_country = get_input_dictionary_city_country()
if dict_city_country:
    find_country()
