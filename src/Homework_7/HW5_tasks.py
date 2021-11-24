"""
Homework5
"""


def hw5_task1():
    dct = {i: i ** 3 for i in range(1, 21)}
    return dct


def hw5_task2(tup=('Odessa', 'Moscow', 'Novgorod'),
              dict_=None):
    if dict_ is None:
        dict_ = {
            1: 'Russia Moscow Petersburg Novgorod Kaluga'.split(),
            2: 'Ukraine Kiev Donetsk Odessa'.split()}
    list_of_countries = []
    for request in tup:
        for cities in dict_.values():
            if request in cities:
                list_of_countries.append(cities[0])
                break
    return list_of_countries


def hw5_task3():
    list_1 = [1, 3, 5]
    list_2 = [1, 3, 5]
    return len(set(list_1) | set(list_2))


def hw5_task4():
    list_1 = [1, 3, 5, 4]
    list_2 = [1, 3, 5, 6]
    return len(set(list_1) ^ set(list_2))


def hw5_task5():
    dict_ = {0: {'English', 'Russian'},
             1: {'Belarusian', 'English', 'Russian'},
             2: {'French', 'Italian', 'Russian'}}
    all_know = set()
    one_know = set()
    for key in dict_:
        lang = dict_[key]
        all_know |= lang
        one_know ^= lang
    return f'Students know everything {len(all_know)} languages.\n It\'s: {all_know}\n' \
           f' At least one knows {len(one_know)} languages.\n It\'s {one_know}'


def hw5_task6(str_: str = 'Trump hit back, 11 repeated '
                          '\n again hit 222    false \n 11 claim that the '):
    for char in str_:
        if (not char.isalpha()) and char != ' ':
            str_ = str_.replace(char, "")
    str_ = set(str_.lower().split())
    return f'The text contains {len(str_)} different words'


def hw5_task7(num_1=6, num_2=8, nod=0):
    while num_1 != 0:
        if num_1 > num_2:
            num_1, num_2 = num_2, num_1
        elif num_2 % num_1 == 0:
            nod = num_1
            break
        else:
            num_2 %= num_1
    return nod
