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

# Крайняя конструкция (начиная с 44 строки):
# перебор списка O(N)
# перебор ключей словаря O(N)
# проверка вхождения O(N)
# в итоге O(N)*O(N)*O(N) = O(N^3)
num_of_country = int(input('How much countries would you like input: '))
list_of_countries = [input('Input countries and cities+"Space": ') for _ in range(num_of_country)]
num_of_req = int(input('How much requests would you like input: '))
list_of_request_cities = [input('Enter cities + "Enter": ') for _ in range(num_of_req)]
total_list = []
dict_of_countries = {}

for char in list_of_countries:
    total_list.append(char.split())

for i in range(num_of_country):
    dict_of_countries[total_list[i][0]] = total_list[i][1:]

for city in list_of_request_cities:
    for country in dict_of_countries:
        if city in dict_of_countries[country]:
            print(country)
