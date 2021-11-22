'''В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list. 
Откройте и прочитайте файл(если его нет необходимо вывести ошибку). 
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
'''

import json


def imdb_sort(input_file):
    line_number = 0
    with open(input_file, 'r') as file:
        top250 = file.readlines()
        list_1 = top250[28:278]

    fh = open('ratings.txt', 'w')

    for i in list_1:
        b = i.split('   ')
        c = b[-1].split('  ')
        print(c)

    fh.close()


imdb_sort('data_hw7/ratings.list')
