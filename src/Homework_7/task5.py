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


def pars(file):
    try:
        dict_of_ratings = {}
        dict_of_year = {}
        top_250_str = []
        fh = codecs.open(file, 'r', encoding='utf-8', errors='ignore')
        top_250 = open('top250_movies.txt', 'w')
        ratings = open('ratings.txt', 'w')
        years = open('years.txt', 'w')
        data = fh.readlines()
        list_of_250 = data[28:278]
        for line in list_of_250:
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
        json.dump(top_250_str, top_250, indent=4)
        json.dump(dict_of_ratings, ratings, indent=4)
        json.dump(dict_of_year, years, indent=4)

        def draw_gist(dict_):
            dictionary = {key: len(dict_[key]) for key in dict_}
            sorted_list = sorted([dictionary[key] for key in dictionary])
            sorted_dic = {}
            for elem in sorted_list:
                for key in dictionary:
                    if elem == dictionary[key]:
                        sorted_dic[key] = dictionary[key]
            plt.bar(list(sorted_dic.keys()), sorted_dic.values(), color='g')
            return plt.show()

        draw_gist(dict_of_year)
        draw_gist(dict_of_ratings)
        top_250.close()
        ratings.close()
        years.close()
        fh.close()

    except FileNotFoundError:
        print('File not found.')


pars('ratings.list')
