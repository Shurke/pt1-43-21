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


import matplotlib.pyplot as plt
import seaborn


def read_file():
    """returns list of file lines"""

    try:
        with open('ratings.list', 'r') as ratings_list_file:
            top_250_films = ratings_list_file.readlines()
            return top_250_films
    except FileNotFoundError:
        print('Ошибка - файл не найден')


def writing_in_the_file(file_name, given_dict):
    """creates histogram in the given file"""

    plt.figure(figsize=(10, 4))
    seaborn.barplot(x=list(given_dict.keys()), y=list(given_dict.values()))
    plt.xticks(rotation=90)
    plt.savefig(file_name)
    # plt.show()
    print(f'Файл {file_name} создан')


def write_top250txt(titles):
    """Creates file with titles of the best 250 movies"""

    with open('top250_movies.txt', 'w') as top250:
        for title in titles:
            top250.write(title + '\n')
    print('Файл top250_movies.txt создан')


def processing_file(input_file):
    """function processes input file with rates"""

    titles = []
    years = []
    rates = []
    dict_years = {}
    dict_rates = {}
    for element in input_file[28:278]:
        str_element = element.strip()
        list_of_data = str_element.split('  ')
        titles.append(list_of_data[-1][:-7])   # appends title
        years.append(list_of_data[-1][-5:-1])  # appends years
        rates.append(list_of_data[-2][1:])     # appends rates
    for year in years:
        if year not in dict_years.keys():
            dict_years[year] = years.count(year)
    for rate in rates:
        if rate not in dict_rates.keys():
            dict_rates[rate] = rates.count(rate)
    writing_in_the_file('rates.jpeg', dict_rates)
    writing_in_the_file('years.jpeg', dict_years)
    write_top250txt(titles)


def main():
    processing_file(read_file())


main()
