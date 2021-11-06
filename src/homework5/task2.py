'''
2. Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия городов
этой страны. В следующей строке записано число M, далее идут
M запросов — названия каких-то M городов, перечисленных выше.
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
'''


N = int(input('Введите количество стран: '))
current_dict = {}
countries_all = {}

for i in range(N):
    country_input = input('Введите строку страны: ')
    country_list = country_input.split(' ')
    country_name = country_list.pop(0)
    current_dict = current_dict.fromkeys(country_list, country_name)
    countries_all.update(current_dict)

M = int(input('Кол-во запросов: '))
countries_res = str()

for i in range(M):
    town_input = input('Город: ')
    countries_res = countries_res + countries_all[town_input] + '\n'

print(countries_res)
