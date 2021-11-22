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
    tmp_file = open(fl_name, "w")
    tmp_lst = sorted(in_lst, key=lambda x: x[sort_ind])
    for item in tmp_lst:
        tmp_file.write(str(item[sort_ind]) + ' | ' + item[out_ind] + '\n')
    tmp_file.close()


def main():
    try:
        with open('ratings.list', 'r', encoding='utf-8', errors='ignore') as fh:
            lines = fh.readlines()
            result_list = []
            # Create TOP250 list
            start_found = 0
            stop_found = 0
            start_ind = 0
            stop_ind = 0
            ind = 0
            # Search for top 250 line index
            for item in lines:
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
            top_250_list = lines[start_ind + 1:stop_ind:]
            for line in top_250_list:
                tmp_lst = line.split()
                tmp_rank = float(tmp_lst[2])
                tmp_name = " ".join(tmp_lst[3:-1])
                tmp_year = int(tmp_lst[-1].strip('(').strip(')').strip('/I'))
                result_list.append([tmp_rank, tmp_name, tmp_year])

            # Make files
            # Top 250. Names
            tmp_file = open("top250_movies.txt", "w")
            ind = 1
            for item in result_list:
                tmp_file.write(str(ind) + ' | ' + item[1] + '\n')
                ind += 1
            tmp_file.close()

            # Top 250. Ratings
            make_file("ratings.txt", result_list, 0, 1)

            # Top 250. Years
            make_file("years.txt", result_list, 2, 1)

            print('Finished!')

    except FileNotFoundError:
        print('File not found')


main()
