"""
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
"""


print("Программа выдает страну, в которой находится указанный город.")
number_of_countries = int(input("Введите количество стран, с которым хотите работать: "))
i = 0
dict_of_names = {}
while i < number_of_countries:
    country = input(f"Введите страну №{i+1} и города в формате "
                    f"'Страна Город 1 Город 2 Город 3 итд': ")
    list_of_names = country.split()
    country = list_of_names.pop(0)
    dict_of_names[country] = list_of_names
    i += 1
number_of_cities = int(input("Введите количество городов, с которым хотите работать: "))
i = 0
list_of_counties = []
country = ""
while i < number_of_cities:
    city_for_search = input(f"Введите город №{i + 1}: ")
    for country in dict_of_names:
        if city_for_search in dict_of_names.get(country):
            list_of_counties.append(country)
    i += 1
num = 0
for country in list_of_counties:
    num += 1
    print(f"Страна города №{num}: {country}")
