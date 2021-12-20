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


from task3_list_of_countries import result_list_of_countries


def task2(tup_of_req: [list, tuple] = None, dict_of_cities: dict = None):
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
    if type(tup_of_req).__name__ not in ('tuple', 'list'):
        raise TypeError("Data contained request with cities for check transmits in function with"
                        " 'tuple' or 'list' type!")
    elif type(dict_of_cities).__name__ != 'dict':
        raise TypeError("You need to pass to the function a dictionary!")
    # this loop breaks the string into elements and converts it to list
    for key, val in dict_of_cities.items():
        dict_of_cities[key] = val.split()

    # this block check:
    #   the key should be a number only
    #   country name must come first: it compare the first element in list with
    #   auxiliary list - result_list_of_countries
    #   names of cities and countries contain only letters
    #   city and country name must start with a capital letter
    #   and check the length of the city name
    for key, city_list in dict_of_cities.items():
        if type(key).__name__ != 'int':
            raise TypeError('The key in dictionary must be a integer!')
        elif city_list[0] not in result_list_of_countries:
            raise TypeError('The name of the country should be in the first place!')
        for elem in city_list:
            if type(elem).__name__ != 'str' or not elem.isalpha():
                raise TypeError('Names of cities and countries must contain only letters!')
            elif elem.islower():
                raise TypeError('City and country name must start with a capital letter')
            elif len(elem) <= 1:
                raise TypeError('There are no cities with this name.')

    # this block check the name of cities in requests list
    for city in tup_of_req:
        if type(city).__name__ != 'str' or not city.isalpha():
            raise TypeError('The city name cannot contain numbers!')
        elif city[0].islower():
            raise TypeError('City name must start with a capital letter')

    # this loop forms a result list with the names of countries for output
    for request in tup_of_req:
        for cities in dict_of_cities.values():
            if request in cities:
                result.append(cities[0])
                break
    return ' '.join(result)
