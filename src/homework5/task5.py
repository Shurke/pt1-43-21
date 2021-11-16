"""Задача 5. Языки

Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
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
"""


def get_languages():
    """функция возвращает языки, которые знают школьники"""
    try:
        quantity_of_schoolchildren = int(input("Введите количество школьников: "))
    except ValueError:
        print("Это не число")
        return
    list_of_schoolchildren = list()
    for i in range(quantity_of_schoolchildren):
        try:
            quantity_of_languages = int(input("Введите количество языков,"
                                              " которые знает школьник: "))
        except ValueError:
            print("Это не число")
            return
        set_i = set()
        for j in range(quantity_of_languages):
            set_i.add(input("Введите язык: "))
        list_of_schoolchildren.append(set_i)
    known_by_everybody = set.intersection(*list_of_schoolchildren)
    known_by_somebody = set.union(*list_of_schoolchildren)
    print(f"языки, котрые знают все школьники: {len(known_by_everybody)}",
          *known_by_everybody, sep="\n")
    print(f"языки, котрые знает хотя бы один школьник: {len(known_by_somebody)}",
          *known_by_somebody, sep="\n")


get_languages()
