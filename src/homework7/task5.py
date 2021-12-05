"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b. Найдите ТОП250 фильмов и извлеките заголовки.
c. Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""


import os


def movies():
    if os.path.exists('ratings.list.txt'):
        content = read_file('ratings.list.txt')
        top250 = []
        ratings = {}
        years = {}
        for item in content:
            top250.append(item[6].strip().replace('\n', '')[:-7])
            rate = item[5].strip()
            if rate in ratings:
                ratings[rate] += 1
            else:
                ratings[rate] = 1
            year = item[6].strip()[-5:-1]
            if year in years:
                years[year] += 1
            else:
                years[year] = 1
        ratings_sorted = dict_sorting_keys(ratings, True)
        years_sorted = dict_sorting_keys(years, True)
        write_file('top250_movies.txt', top250)
        write_file('ratings.txt', ratings_sorted)
        write_file('years.txt', years_sorted)
    else:
        print('Файл `ratings.list.txt` не существует по указанному пути.')


def dict_sorting_keys(dict_, rev=False):
    keys = list(dict_.keys())
    keys.sort(reverse=rev)
    dict_sorted = {}
    for i in keys:
        dict_sorted[i] = dict_[i]
    return dict_sorted


def read_file(filename):
    n = 0
    find_start = 0
    content = []
    with open(filename, 'r') as file:
        for line in file:
            if 0 < n < 251:
                content.append(line.split('  '))
                n += 1
            if find_start == 0 and line.find('New  Distribution  Votes  Rank  Title') != -1:
                n = 1
                find_start = 1
    file.close()
    return content


def write_file(filename, data):
    with open(filename, 'w') as file:
        if isinstance(data, list):
            for item in data:
                file.write(item + "\n")
        if isinstance(data, dict):
            for key, value in data.items():
                file.write(key + ": " + str(value) + "\n")
    file.close()
    print('Запись в файл', filename, 'закончена.')


movies()
