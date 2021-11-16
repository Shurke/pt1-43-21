"""
Языки
Каждый из N школьников некоторой школы знает Mi языков.
Определите,
какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество
школьников N. Далее идет N чисел Mi,
после каждого из чисел идет Mi строк,
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
В первой строке выведите количество языков,
которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков,
которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""


def main():
    students_num = int(input('Введите количество школьников: '))
    students_languages = []
    for _ in range(students_num):
        print('Введите количество языков, которое знает школьник: ', end='')
        languages_num = int(input())
        languages = {input('Язык - ') for _ in range(languages_num)}
        students_languages.append(languages)
    all_known_languages = students_languages[0]
    at_least_one_known = students_languages[0]
    for element in students_languages:
        all_known_languages = all_known_languages & element
        at_least_one_known.update(element)
    print('Количество языков, которые знают все школьники -', end=' ')
    print(len(all_known_languages), '\n', all_known_languages)
    print('Количесвто языков, которые знает хотя бы 1 школьник -', end=' ')
    print(len(at_least_one_known), '\n', at_least_one_known)


main()
