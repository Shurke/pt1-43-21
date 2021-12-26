"""
Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами. Учтите, что
в функцию могут быть переданы некорректные значения, здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама.
Вариант 10
Домашняя 5. Задача 4(4я задача простая, брал 2ю).

task2
Города
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается
с названия страны, затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
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


def task2(tup_of_req=None, dict_of_cities=None):
    """
    The function input num of
    :param tup_of_req: it contain the cities that we want to check
    :param dict_of_cities: it contain num of countries as key and string with the first
    of the country name and list of cities as value
    :return: the name of the countries in which the cities from the tup_of_req are located
    """
    result = []
    if tup_of_req is None and dict_of_cities is None:
        # if the function does not contain arguments, the user is prompted to enter them manually
        num_of_req = int(input('Enter num of req: '))
        tup_of_req = tuple(input('Enter requests city + "Enter": ')
                           for _ in range(num_of_req))
        num_of_country = int(input('Enter num of country: '))
        dict_of_cities = {i: input('Enter country and cities per space: ')
                          for i in range(num_of_country)}
    # this block check the type of object that transmit in function
    elif type(tup_of_req).__name__ not in ('tuple', 'list') or\
            type(dict_of_cities).__name__ != 'dict':
        raise TypeError("Incorrect input data type!")

    # this loop breaks the string into elements and converts it to list
    for key, val in dict_of_cities.items():
        dict_of_cities[key] = val.split()
    # this block check:
    #   names of cities and countries contain only letters
    #   city and country name must start with a capital letter
    #   and check the length of the city name
    for city_list in dict_of_cities.values():
        for elem in city_list:
            if any([type(elem).__name__ != 'str',
                    not elem.isalpha(),
                    elem.islower(),
                    len(elem) <= 1]):
                raise TypeError('City and country names must be longer than 1,'
                                ' start with a capital letter, and contain only letters.')
    # this block check the name of cities in requests list
    for city in tup_of_req:
        if type(city).__name__ != 'str' or not city.isalpha():
            raise TypeError('The city name cannot contain numbers!')
        if city[0].islower():
            raise TypeError('City name must start with a capital letter')

    # this loop forms a result list with the names of countries for output
    for request in tup_of_req:
        for cities in dict_of_cities.values():
            if request in cities:
                result.append(cities[0])
                break
    return ' '.join(result)
