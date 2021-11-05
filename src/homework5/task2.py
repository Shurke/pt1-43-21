'''
2.Города
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.

Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число M,
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
'''


def main():
    main_dict = {}
    output_lst = []
    # input processing
    for ind in range(int(input('Введите количество записей:'))):
        country, *cities = input('Введите запись:').split()
        for city in cities:
            # key should be unique
            main_dict[city] = country

    # output processing
    for ind in range(int(input('Введите количество городов:'))):
        output_lst.append(str(input('Введите город:')))

    print('Result')
    for element in output_lst:
        print(main_dict[element])


main()
