"""
    Города

    Дан список стран и городов каждой страны. Затем даны названия
    городов. Для каждого города укажите, в какой стране он находится.

    Входные данные

    Программа получает на вход количество стран N. Далее идет N
    строк, каждая строка начинается с названия страны, затем идут
    названия городов этой страны. В следующей строке записано число
    M, далее идут M запросов — названия каких-то M городов, перечисленных выше.

    Выходные данные

    Для каждого из запроса выведите название страны, в
    котором находится данный город.

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
