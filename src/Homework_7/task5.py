"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt –
гистограмма рейтингов, years.txt – гистограмма годов.
"""


import codecs
import json
import matplotlib.pyplot as plt


top_250_str = []
dict_of_year = {}
dict_of_ratings = {}


def date_generator(file_name, key=None, band=None):
    """Function generate rows in entered range after key-word"""
    if key is None:
        key = "New  Distribution "
    if band is None:
        band = 250
    try:
        fh = codecs.open(file_name, 'r', encoding='utf-8', errors='ignore')
        while key not in fh.readline():
            fh.readline()
            next(fh)
        for i in range(band):
            yield next(fh)
    except FileNotFoundError:
        print('File not found.')


def date_operate(generator_func):
    """Function add data to objects"""
    for line in generator_func:
        line = line.split()[2:]
        temp_str = ''
        for i in line[1:-1]:
            temp_str += i + ' '
        temp_str = temp_str[:-1]
        top_250_str.append(temp_str)
        if line[0] not in dict_of_ratings:
            dict_of_ratings[line[0]] = list([temp_str])
        else:
            dict_of_ratings[line[0]].append(temp_str)
        if line[-1][1:-1] not in dict_of_year:
            dict_of_year[line[-1][1:-1]] = list([temp_str])
        else:
            dict_of_year[line[-1][1:-1]].append(temp_str)


def draw_gist(date_dict):
    """Function for histograms drawing"""
    dictionary = {key: len(date_dict[key]) for key in date_dict}
    sorted_list = sorted([dictionary[key] for key in dictionary])
    sorted_dic = {}
    for elem in sorted_list:
        for key in dictionary:
            if elem == dictionary[key]:
                sorted_dic[key] = dictionary[key]
    plt.bar(list(sorted_dic.keys()), sorted_dic.values(), color='g')
    return plt.show()


def write_file(name=None, *args, **kwargs):
    """Function create .txt file with name - 'name' and data from iter object"""
    if name is None:
        name = 'Default.txt'
    name += '.txt'
    if len(args) == 0:
        data = kwargs
    else:
        data = args
    file = open(name, 'w')
    json.dump(data, file, indent=4)


date = date_generator('ratings.list')
date_operate(date)

write_file('top250_movies', top_250_str)
write_file('ratings', dict_of_ratings)
write_file('years', dict_of_year)

draw_gist(dict_of_ratings)
draw_gist(dict_of_year)
