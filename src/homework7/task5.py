"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""


def read_file():
    """Функция читает файл и возвращает список строк с рейтингом 250 фильмов"""
    filename = "data/ratings.list.txt"
    list_of_strings = list()
    start_line = "New  Distribution  Votes  Rank  Title"
    end_line = ""
    info_started = False
    try:
        with open(filename, "r", encoding="ISO-8859-1") as f:
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


def rating_generation(strings):
    """Функция преобразует список строк в кортеж, с которым удобнее работать"""
    list_of_rate = list()
    for string in strings:
        list_of_words = string.split()
        year = int(list_of_words[-1][1:5])
        rank = float(list_of_words[2])
        name = " ".join(list_of_words[3:-1])
        list_of_rate.append((rank, year, name))
    return list_of_rate


def writing_file_top(rate):
    """Функция создает файл с названием 'top250_movies.txt'"""
    with open("top250_movies.txt", "w") as file_top_250:
        for inform in rate:
            file_top_250.write(inform[2] + '\n')
    print("Создан файл top250_movies.txt")


def bar_generation(list_of_items, file_name):
    """Функция создает графичискую гистограмму"""
    set_of_items = set(list_of_items)
    list_of_items_short = list(set_of_items)
    list_of_items_short.sort()
    with open(file_name, "w") as file:
        for item in list_of_items_short:
            bar_string = str(item) + "   "
            for i in range(list_of_items.count(item)):
                bar_string = bar_string + "|"
            file.write(bar_string + '\n')
    print(f"Создан файл {file_name}")


def imbd_ratings():
    """Функция создает 3 файла

    top250_movies.txt – названия файлов,
    ratings.txt – гистограмма рейтингов,
    years.txt – гистограмма годов.
    """
    list_of_strings = read_file()
    list_of_rate = rating_generation(list_of_strings)
    writing_file_top(list_of_rate)
    list_of_rating = list(x[0] for x in list_of_rate)
    bar_generation(list_of_rating, "data/ratings.txt")
    list_of_years = list(x[1] for x in list_of_rate)
    bar_generation(list_of_years, "data/years.txt")


imbd_ratings()
