"""
5.	В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
в файле ./data_hw5/ ratings.list.
a.	Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b.	Найдите ТОП250 фильмов и извлеките заголовки.
c.	Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""
import os

path = 'ratings.list'
ratings = dict()
if os.path.exists(path):
    fh = open(path, 'r', encoding="ISO-8859-1")
    data = fh.readlines()
    list_ = data[28:278]
    for item1 in list_:
        n = 0
        a = item1.split()
        title = a[3:-1:]
        title = ' '.join(title)
        ftitle = open('top250_movies.txt', 'a')
        ftitle.write(title + '\n')
        ftitle.close()
        rank = a[2]
        frank = open('ratings.txt', 'a')
        frank.write('{}: {}\n'.format(title, rank))
        frank.close()
        year = a[-1].replace('(', '').replace(')', '')
        fyear = open('years.txt', 'a')
        fyear.write('{}: {}\n'.format(title, year))
        fyear.close()
    fh.close()
    print(type(ratings))
else:
    print('Error')
