def get_movies_ratings():
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
        # Получение списка строк
        movie_list = get_line_list()

        # Создание словарей
        list_dict = get_dictionaries(movie_list)

        # Упорядочивание данных в словарях
        sort_movie_list = sort_dict(list_dict[0])
        sort_rating_list = sort_dict(list_dict[1])
        sort_year_list = sort_dict(list_dict[2])

        # Запись данных  в файлы
        with open('top250_movies.txt', 'w') as movie_name:
            for item1, item2 in sort_movie_list:
                movie_name.write(item2 + '\n')
        with open('ratings.txt', 'w') as movie_rating:
            movie_rating.write('Рейтинг фильма ' + 'Количество фильмов' + '\n')
            for rating, ratings_amount in sort_rating_list:
                temp_str = ' ' * 11 + str(rating) + ' ' * 16 + str(ratings_amount).rjust(3)
                movie_rating.write(temp_str + '\n')
        with open('years.txt', 'w') as movie_year:
            movie_year.write('Год выпуска фильма ' + 'Количество фильмов' + '\n')
            for year, years_amount in sort_year_list:
                temp_str = ' ' * 14 + str(year) + ' ' * 16 + str(years_amount).rjust(3)
                movie_year.write(temp_str + '\n')

    except FileNotFoundError:
        print('Файл не найден!')


def get_line_list():
    """Получение списка строк из файла с 29 по 278"""
    with open('ratings.list', 'r', encoding='latin-1') as movie_file_read:
        start_line_number = 28
        stop_line_number = 278
        movie_line_list = []
        for number_line, line in enumerate(movie_file_read):
            if number_line in range(start_line_number, stop_line_number):
                movie_line_list.append(line)
            elif number_line >= stop_line_number:
                break
    return movie_line_list


def write_dict_value(some_dict, some_value):
    """Запись количества повторов ключа словаря в значение ключа."""
    if some_dict.get(some_value) is None:
        some_dict[some_value] = 1
    else:
        some_dict[some_value] = some_dict[some_value] + 1


def get_dictionaries(movie_line_list):
    """Создание словарей фильмов, гистограмм рейтингов и годов выпуска."""
    dict_movie = {}
    dict_rating = {}
    dict_year = {}
    item = 1
    for movie_line in movie_line_list:
        # Поиск рейтинга по '.' и года выпуска по '('
        rating_index = movie_line.find('.')
        rating_value = float(movie_line[rating_index - 1: rating_index + 2])
        year_index = movie_line.find('(')
        year_value = int(movie_line[year_index + 1: year_index + 5])

        # Выделение названия фильма по положению точки и скобки
        movie_value = movie_line[rating_index + 4: year_index - 1]

        # Создание словаря названий фильмов
        dict_movie[item] = movie_value

        # Создание словарей по рейтингу и году
        write_dict_value(dict_rating, rating_value)
        write_dict_value(dict_year, year_value)
        item += 1
    return [dict_movie, dict_rating, dict_year]


def sort_dict(input_dict):
    """Сортировка словаря по ключу в список."""
    return sorted(input_dict.items(), key=lambda x: x[0])


get_movies_ratings()
