"""
    Работа с файлами:

    В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
    в файле /ratings.list.
        a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
        b. Найдите ТОП250 фильмов и извлеките заголовки.
        c. Программа создает 3 файла  top250_movies.txt – названия файлов,
        ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""

# Проверка наличия файла
try:
    movie_file_read = open('ratings.list', 'r', encoding='latin-1')
    movie_name = open('top250_movies.txt', 'w')
    dict_movie = {}
    dict_rating = {}
    dict_year = {}

    for item, line in enumerate(movie_file_read):
        if item in range(28, 278):
            # Поиск '.' (рейтинг) и '(' (год выпуска)
            rating_index = line.find('.')
            rating_value = float(line[rating_index - 1: rating_index + 2])
            year_index = line.find('(')
            year_value = int(line[year_index + 1: year_index + 5])
            # Выделение названия фильма по положению точки и скобки
            movie_value = line[rating_index + 4: year_index - 1]
            movie_name.write(movie_value + '\n')
            # Создания словаря по месту в рейтинге
            dict_movie[item - 27] = [movie_value, rating_value, year_value]

            # Создание словарей по рейтингу и году
            if dict_rating.get(rating_value) is None:
                dict_rating[rating_value] = 1
            else:
                dict_rating[rating_value] = dict_rating[rating_value] + 1
            if dict_year.get(year_value) is None:
                dict_year[year_value] = 1
            else:
                dict_year[year_value] = dict_year[year_value] + 1

    movie_name.close()
    movie_file_read.close()
    # Упорядочивание данных в словарях
    sort_year_list = sorted(dict_year.items(), key=lambda x: x[0])
    sort_rating_list = sorted(dict_rating.items(), key=lambda x: x[0])

    # Запись данных  в файлы ratings.txt, years.txt
    movie_rating = open('ratings.txt', 'w')
    movie_rating.write('Рейтинг фильма ' + 'Количество фильмов' + '\n')
    for item1, item2 in sort_rating_list:
        movie_rating.write(' ' * 11 + str(item1) +
                           ' ' * 16 + str(item2).rjust(3) + '\n')
    movie_rating.close()
    movie_year = open('years.txt', 'w')
    movie_year.write('Год выпуска фильма ' + 'Количество фильмов' + '\n')
    for item1, item2 in sort_year_list:
        movie_year.write(' ' * 14 + str(item1) +
                         ' ' * 16 + str(item2).rjust(3) + '\n')
    movie_year.close()

except FileNotFoundError:
    print('Файл не существует!')
