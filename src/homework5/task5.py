'''
5.Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.

Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
'''


def main():
    all_students_dct = {}
    one_lang = set()
    # input processing
    in_num_of_stud = int(input('Введите количество школьников:'))
    for ind1 in range(in_num_of_stud):
        languages_lst = []
        in_num_of_lang = int(input('Введите количество языков:'))
        for ind2 in range(in_num_of_lang):
            languages_lst.append(input('Введите язык:'))
        one_lang = one_lang | set(languages_lst)
        all_students_dct[ind1] = languages_lst

    # output processing
    # If leave common_lang as (), the result will be empty set
    common_lang = set(all_students_dct.get(0))
    for ind1 in range(len(all_students_dct.values())):
        tmp_set = set(all_students_dct.get(ind1))
        common_lang = common_lang & tmp_set

    print('Кол-во общих языков:', len(common_lang))
    print('Языки:')
    for ind1 in common_lang:
        print(ind1)

    print('Кол-во общих языков, которые знает хотя бы один школьник:', len(one_lang))
    print('Языки:')
    for ind1 in one_lang:
        print(ind1)


main()
