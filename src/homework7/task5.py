"""
5.	В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
a.	Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b.	Найдите ТОП250 фильмов и извлеките заголовки.
c.	Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""
import os

path = 'ratings.list'
if os.path.exists(path):
    fh = open(path, 'r', encoding="ISO-8859-1")
    data = fh.readlines()
    list_ = data[28:278]
    for item1 in list_:
        n = 0
        a = item1.split()
        a = a[3::]
        a = ' '.join(a)
        print(a)
    fh.close()
else:
    print('Error')
