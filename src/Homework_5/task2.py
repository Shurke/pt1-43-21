"""
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


def task2(tup_of_req, dict_of_cities):
    for request in tup_of_req:
        for cities in dict_of_cities.values():
            if request in cities:
                print(cities[0])
                break


if __name__ == "__main__":
    task2(tup_of_req=('Odessa', 'Moscow', 'Novgorod'),
          dict_of_cities={1: 'Russia Moscow Petersburg Novgorod Kaluga'.split(),
                          2: 'Ukraine Kiev Donetsk Odessa'.split()})
