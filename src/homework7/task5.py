'''
Работа с файлами:
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
'''


def make_file(fl_name, in_lst, sort_ind, out_ind):
    with open(fl_name, "w") as f:
        tmp_lst = sorted(in_lst, key=lambda x: x[sort_ind])
        for item in tmp_lst:
            f.write(str(item[sort_ind]) + ' | ' + item[out_ind] + '\n')


def read_data():
    # Read data from file
    try:
        with open('ratings.list', 'r', encoding='utf-8', errors='ignore') as fh:
            loc_lines = fh.readlines()
            return loc_lines
    except FileNotFoundError:
        print('File not found')


def top250_list_creation(loc_lines, start_ind, stop_ind):
    # Create cleared TOP250 list
    if loc_lines is None:
        return None

    result_list = []
    tmp_list = loc_lines[start_ind + 1:stop_ind:]
    for line in tmp_list:
        tmp_lst = line.split()
        tmp_rank = float(tmp_lst[2])
        tmp_name = " ".join(tmp_lst[3:-1])
        tmp_year = int(tmp_lst[-1].strip('(').strip(')').strip('/I'))
        result_list.append([tmp_rank, tmp_name, tmp_year])
    return result_list


def main(loc_lines):
    # Main algorithm
    if loc_lines is None:
        print('Error')
        return

    result_list = []
    # Create TOP250 list
    start_found = 0
    stop_found = 0
    start_ind = 0
    stop_ind = 0
    ind = 0

    # Search for top 250 line index
    for item in loc_lines:
        tmp_line = item.strip()
        if tmp_line == 'New  Distribution  Votes  Rank  Title':
            start_found = 1
            start_ind = ind
        if start_found and tmp_line == '':
            stop_found = 1
            stop_ind = ind
        if start_found and stop_found:
            break
        ind += 1

    # Result list creation
    result_list = top250_list_creation(loc_lines, start_ind, stop_ind)
    if result_list is None:
        print('Error')
        return

    # Make files
    # Top 250. Names
    with open("top250_movies.txt", "w") as f:
        ind = 1
        for item in result_list:
            f.write(str(ind) + ' | ' + item[1] + '\n')
            ind += 1

    # Top 250. Ratings
    make_file("ratings.txt", result_list, 0, 1)

    # Top 250. Years
    make_file("years.txt", result_list, 2, 1)

    print('Finished!')


lines = read_data()
main(lines)
