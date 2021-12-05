"""    5. В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
        a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
        b. Найдите ТОП250 фильмов и извлеките заголовки.
        c. Программа создает 3 файла  top250_movies.txt – названия файлов,
        ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов."""


ratings = {}
names250 = []
years = {}
with open("ratings.list", 'r') as file:
    top250 = file.readlines()
    top250_n = top250[28:278]

for str_elem in top250_n:
    new_str_elem = str_elem.split('   ')
    rat = new_str_elem[-1].split('  ')
    if rat[0] not in ratings:
        ratings[rat[0]] = 1
    else:
        ratings[rat[0]] += 1

    if rat[-1][-6:-2:] not in years:
        years[rat[-1][-6:-2:]] = 1
    else:
        years[rat[-1][-6:-2:]] += 1

    names250.append(rat[1][:-8:])
    r = open('ratings.txt', 'w')
    for rate in ratings:
        r.write(rate + ' - ')
        r.write(str(ratings[rate]) + '\n')

    y = open('years.txt', 'w')
    for year in years:
        y.write(year + ' - ')
        y.write(str(years[year]) + '\n')

    t = open('top250_movies.txt', 'w')
    for name in names250:
        t.write(name + '\n')
