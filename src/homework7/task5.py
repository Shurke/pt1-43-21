"""Задача5.

В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt
– гистограмма рейтингов, years.txt – гистограмма годов.
"""


def read_file():
    """Функция читает файл и возвращает список строк с рейтингом 250 фильмов"""
    file_name = "ratings.list"
    list_of_strings = list()
    start_line = "New  Distribution  Votes  Rank  Title"
    end_line = ""
    info_started = False
    try:
        with open(file_name, "r", encoding="ISO-8859-1") as f:
            for line in f:
                line_strip = line.strip()
                if not info_started and line_strip == start_line:
                    info_started = True
                elif not info_started and line_strip != start_line:
                    continue
                elif info_started and line_strip == end_line:
                    break
                else:
                    list_of_strings.append(line_strip)
    except FileNotFoundError:
        print("Ошибка чтения файла")
    return list_of_strings


def get_rate(list_of_strings):
    """Получает рейтинг

    Функция из списка строк с фильмами и рейтингами создает список
    кортежей с рейтингом, годом и названием фильма

    """
    list_of_rate = list()
    for item in list_of_strings:
        list_of_words = item.split()
        year = int(list_of_words[-1][1:5])
        rank = float(list_of_words[2])
        name = " ".join(list_of_words[3:-1])
        list_of_rate.append((rank, year, name))
    return list_of_rate


def create_file_top250(list_of_rate):
    """Функция создает файл top250_movies.txt – названия файлов"""
    file_top_250 = open("top250_movies.txt", "w")
    for item in list_of_rate:
        file_top_250.write(item[2] + '\n')
    file_top_250.close()
    print("Создан файл top250_movies.txt")


def create_bar_chart(list_of_items, file_name):
    """Функция создает гистограмму по заданному списку"""
    f = open(file_name, "w")
    set_of_items = set(list_of_items)
    list_of_items_short = list(set_of_items)
    list_of_items_short.sort()
    for item in list_of_items_short:
        bar_string = str(item) + "   "
        for i in range(list_of_items.count(item)):
            bar_string = bar_string + "|"
        f.write(bar_string + '\n')
    f.close()
    print(f"Создан файл {file_name}")


def imbd_ratings():
    """Функция создает 3 файла

    top250_movies.txt – названия файлов, ratings.txt
    – гистограмма рейтингов, years.txt – гистограмма годов.

    """
    list_of_strings = read_file()
    list_of_rate = get_rate(list_of_strings)
    create_file_top250(list_of_rate)
    list_of_rating = list(x[0] for x in list_of_rate)
    create_bar_chart(list_of_rating, "ratings.txt")
    list_of_years = list(x[1] for x in list_of_rate)
    create_bar_chart(list_of_years, "years.txt")


imbd_ratings()
