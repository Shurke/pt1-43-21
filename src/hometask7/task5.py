# -*- coding: utf8 -*-
"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся
в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл
(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""


def read_file():
    """returns list of file lines"""

    try:
        with open('ratings.list', 'r') as ratings_list_file:
            top_250_films = ratings_list_file.readlines()
            return top_250_films
    except FileNotFoundError:
        print('Ошибка - файл не найден')


def processing_file(input_file):
    """function processes input file with rates

    creates 3 new files:
    top250_movies.txt
    ratings.txt
    years.txt

    """

    titles = []
    years = []
    rates = []
    dict_years = {}
    dict_rates = {}
    for element in input_file[28:278]:
        str_element = element.strip()
        list_of_data = str_element.split('  ')
        titles.append(list_of_data[-1][:-7])
        years.append(list_of_data[-1][-5:-1])
        rates.append(list_of_data[-2][1:])
    for year in years:
        if year not in dict_years.keys():
            dict_years[year] = years.count(year)
    for rate in rates:
        if rate not in dict_rates.keys():
            dict_rates[rate] = rates.count(rate)
    with open('top250_movies.txt', 'w') as top250:
        for title in titles:
            top250.write(title + '\n')
    with open('years.txt', 'w') as years_file:
        for element in dict_years:
            content = element + ' - ' + str(dict_years[element]) + '\n'
            years_file.write(content)
    with open('rates.txt', 'w') as rates_file:
        for element in dict_rates:
            content = element + ' - ' + str(dict_rates[element]) + '\n'
            rates_file.write(content)


def main():
    processing_file(read_file())


main()
