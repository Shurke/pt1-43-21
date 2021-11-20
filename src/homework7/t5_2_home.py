"""
2.	Города
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается
с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то M городов,
перечисленных выше.
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


def func():
    n = int(input())
    d = {}
    s = set()
    for item1 in range(n):
        country, *cities = input().split()
        for city in cities:
            d[city] = country
    m = int(input())
    s = [input() for j in range(m)]
    for i in s:
        print(d[i])


if __name__ == "__main__":
    func()
