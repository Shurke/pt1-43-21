"""Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то M городов,
перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры"""

states = {}

for _ in range(int(input('введите колличество стран', ))):
    state, *cities = input('вветите название страны затем названия городов этой строны', ).split()
    for city in cities:
        states[city] = state

print(*(states[input()] for _ in range(int(input(
                                               'введите какое колличество стран хотите запросить и их название', )))), sep="\n")
