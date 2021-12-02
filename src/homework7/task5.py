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
if not os.path.exists(path):
    print('Error')

else:
    def choose_lines():
        with open(path, "r", encoding="ISO-8859-1") as f:
            list_lines = list()
            k = 0
            data = f.readlines()
            line_start = 'New  Distribution  Votes  Rank  Title'
            for line in data:
                if line.strip() == line_start or line.strip() == '' and k > 0:
                    k += 1
                elif k == 1:
                    list_lines.append(line.strip())
                elif k == 2:
                    break
                else:
                    pass
        return list_lines

    def films_list():
        list_films = {}
        for item in choose_lines():
            title = ' '.join(item.split()[3:-1])
            year = item.split()[-1].replace('(', '').replace(')', '')
            rank = item.split()[2]
            list_films[title] = [year, rank]
        return list_films

    def print_films():
        for film in films_list().items():
            with open('top250_movies.txt', 'a') as f:
                f.write(film[0] + '\n')
            with open('ratings.txt', 'a') as f:
                f.write('{}: {}\n'.format(film[0], film[1][1]))
            with open('years.txt', 'a') as f:
                f.write('{}: {}\n'.format(film[0], film[1][0]))

    print_films()
