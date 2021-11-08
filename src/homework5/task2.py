"""
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные:
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные:
Для каждого из запроса выведите название страны, в котором находится данный город.
"""


def main():

    count_countries = int(input('Введите количество стран: '))
    print(count_countries)
    city_country = {}
    for idx in range(count_countries):
        data_line = input('Введите название страны и несколько ее городов через пробел: ')
        data_lst = data_line.split()
        country = data_lst.pop(0)
        for city in data_lst:
            city_country[city] = country
    count_req = int(input('Введите число количества запросов городов: '))
    print(count_req)
    countries = []
    for idx in range(count_req):
        city_name = input('Введите название города из вышеуказанных вариантов: ')
        countries.append(city_country[city_name])
    for cname in countries:
        print(cname)


if __name__ == "__main__":
    main()
