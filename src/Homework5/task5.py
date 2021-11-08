"""
    Языки

    Каждый из N школьников некоторой школы знает Mi языков.
    Определите, какие языки знают все школьники и языки,
    которые знает хотя бы один из школьников.

    Входные данные

    Первая строка входных данных содержит количество школьников N.
    Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
    содержащих названия языков, которые знает i-й школьник.

    Пример входных данных:

    3    # N количество школьников

    2    # M1 количество языков первого школьника

    Russian
    English # языки первого школьника

    3    # M2 количество языков второго школьника

    Russian
    Belarusian
    English

    3

    Russian
    Italian
    French

    Выходные данные

    В первой строке выведите количество языков, которые знают
    все школьники. Начиная со второй строки - список таких языков.
    Затем - количество языков, которые знает хотя бы один
    школьник, на следующих строках - список таких языков.
"""

number_student = int(input('Количество школьников: '))
language_dict = {}
for i in range(number_student):
    language_list = []
    number_language = int(input('Введите количество языков школьника: '))
    for j in range(number_language):
        language_list.append(input('Введите язык: '))
    language_dict[i] = language_list
    # Получение словаря, где ключи - номера школьников.
    # Значения словаря - списки (list) языков школьников.
all_language = set(language_dict.get(0))  # Задать начальное значение
least_one_language = set()
for i in range(len(language_dict.values())):
    all_language = all_language & set(language_dict.get(i))
    least_one_language = least_one_language | set(language_dict.get(i))
print('Количество языков, которые знают все школьники: ', len(all_language))
[print(i) for i in all_language]
print('Количество языков, которые знает хотя бы один школьник: ',
      len(least_one_language))
[print(i) for i in least_one_language]
