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


num_of_country = int(input('How much countries would you like input: ')) #2
list_of_countries = [input('Input countries and cities through a "Space": ') for _ in range(num_of_country)]
#['Russia Moscow Petersburg Novgorod Kaluga', 'Ukraine Kiev Donetsk Odessa']
num_of_req = int(input('How much requests would you like input: ')) #3
list_of_request_cities = [input('Enter the city + "Enter": ') for _ in range(num_of_req)]
#['Odessa', 'Moscow', 'Novgorod']
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
