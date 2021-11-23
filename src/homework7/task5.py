"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b. Найдите ТОП250 фильмов и извлеките заголовки.
c. Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""


import os


def movies():
    if os.path.exists('ratings.list'):
        n = 0
        find_start = 0
        content = []
        with open('ratings.list', 'r') as file:
            for line in file:
                if 0 < n < 251:
                    content.append(line.split('  '))
                    n += 1
                if find_start == 0 and line.find('New  Distribution  Votes  Rank  Title') != -1:
                    n = 1
                    find_start = 1
        file.close()
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
        ratings_keys = list(ratings.keys())
        ratings_keys.sort(reverse=True)
        ratings_sorted = {}
        for i in ratings_keys:
            ratings_sorted[i] = ratings[i]
        years_keys = list(years.keys())
        years_keys.sort(reverse=True)
        years_sorted = {}
        for i in years_keys:
            years_sorted[i] = years[i]
        with open('top250_movies.txt', 'w') as file:
            for item in top250:
                file.write(item + "\n")
        file.close()
        with open('ratings.txt', 'w') as file:
            for key, value in ratings_sorted.items():
                file.write(key + ": " + str(value) + "\n")
        file.close()
        with open('years.txt', 'w') as file:
            for key, value in years_sorted.items():
                file.write(key + ": " + str(value) + "\n")
        file.close()
    else:
        print('Файл `ratings.list` не существует по указанному пути.')


movies()
