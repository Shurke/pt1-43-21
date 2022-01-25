'''В файле хранятся данные с сайта IMDB. Скопированные данные
хранятся в файле ./data_hw5/ ratings.list.
a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b. Найдите ТОП250 фильмов и извлеките заголовки.
c. Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
'''


import re


line_start_number = 29
line_end_number = 278


def histogram(lst_):
    lst_.sort()
    result = ''
    histogram_dct = {}
    for elem in lst_:
        histogram_dct[elem] = histogram_dct.get(elem, '') + '*'
    for key, value in histogram_dct.items():
        result += f'{key}: {value}\n'
    return result


try:
    with open('ratings.list.txt') as fh:
        all_lst = fh.readlines()
        index = 0
        top_250 = []
        ratings = []
        years = []

        for element in all_lst:
            index += 1
            if index >= line_start_number:
                top_250 += re.findall(r'(?<=\d\.\d\s{2}).+(?=\s\()', element)
                ratings += re.findall(r'\d\.\d', element)
                years += re.findall(r'(?<=\()\d{4}', element)

            if index == line_end_number:
                break

    years_histogram = histogram(years)
    ratings_histogram = histogram(ratings)

    with open('./top250_movies.txt', 'a') as movies:
        movies.write('\n'.join(top_250))
    with open('./ratings.txt', 'a') as ratings:
        ratings.write(ratings_histogram)
    with open('./years.txt', 'a') as years:
        years.write(years_histogram)

except FileNotFoundError:
    print('Файл не найден')
