"""
Города
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с
названия страны, затем идут названия городов этой страны. В следующей строке записано число M,
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


def main():
    new_dict = {}
    for i in range(int(input('Введите количество стран: '))):
        str_ = input().split()
        new_dict.update({element: str_[0] for element in str_[1:]})
    requests = [input() for _ in range(int(input('Введите количество запросов: ')))]
    for i in requests:
        print(new_dict[i])


main()
