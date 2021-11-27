'''В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
'''


def imdb_sort(input_file):
    '''Читает файл с рейтингом imdb, создает 3 файла:
    top250_movies.txt – названия файлов,
    ratings.txt – гистограмма рейтингов,
    years.txt – гистограмма годов.
    '''

    rates_dict = {}
    names_list = []
    years_dict = {}
    try:
        with open(input_file, 'r') as file:
            top250 = file.readlines()
            top250_info_all = top250[28:278]  # собираем список информации для обработки

        for film_info_all in top250_info_all:
            film_info_intermediate = film_info_all.split('   ')  # чистим строку
            film_info = film_info_intermediate[-1].split('  ')  # выжимаем
            '''film_info - Представление каждой строки в виде списка со значениями
            ['rating', 'name (year)']
            '''

            if film_info[0] not in rates_dict:
                rates_dict[film_info[0]] = 1
            else:
                rates_dict[film_info[0]] += 1

            if film_info[-1][-6:-2:] not in years_dict:
                years_dict[film_info[-1][-6:-2:]] = 1
            else:
                years_dict[film_info[-1][-6:-2:]] += 1

            names_list.append(film_info[1][:-8:])
        file.close()

        fh = open('ratings.txt', 'w')
        for rate in rates_dict:
            fh.write((rate) + ' - ')
            fh.write(str(rates_dict[rate]) + '\n')
        fh.close()

        fh = open('years.txt', 'w')
        for year in years_dict:
            fh.write((year) + ' - ')
            fh.write(str(years_dict[year]) + '\n')
        fh.close()

        fh = open('top250_movies.txt', 'w')
        for name in names_list:
            fh.write((name) + '\n')
        fh.close()
    except FileNotFoundError:
        print('File does not exist. Make sure that ''ratings.list'' is in data_hw7/ directory')


imdb_sort('data_hw7/ratings.list')
