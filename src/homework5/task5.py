'''
5. Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
которые знает i-й школьник.
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
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков.
'''


number_of_pupils = int(input('Введите количество школьников: '))
language_pool = set()
list_lang = list()

for i in range(number_of_pupils):
    number_of_languages = int(input('Введите количество языков, которые знает школьник: '))
    language = ''
    for i in range(number_of_languages):
        language = input('Введи язык: ')
        list_lang.append(language)

language_pool = set(list_lang)  # Языки, которые знает хотя бы один школьник
common_languages = list()

for lang in list_lang:
    if list_lang.count(lang) == number_of_pupils and lang not in common_languages:
        common_languages.append(lang)  # Создаем список общих языков для всех

print(f'Количество языков, которые знают все школьники - {len(common_languages)}')
print('Список языков, которые знают все школьники:\n' + '\n'.join(common_languages))
print(f'Количество всех языков, известных школьникам - {len(language_pool)}')
print('Список всех языков, известных школьникам:\n' + '\n'.join(language_pool))
