"""
Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все
школьники и языки, которые знает хотя бы один из школьников.
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
В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки -
список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на следующих
строках - список таких языков.
"""


num_of_scholar = 3
#int(input())
list_of_lang = []
#[{'English', 'Russian'}, {'Belarusian', 'English', 'Russian'}, {'French', 'Italian', 'Russian'}]
all_know = set()
one_know = set()

for i in range(num_of_scholar):
    temp_set = set()
    for j in range(int(input("Enter the number of languages: "))):
        temp_set.add(input('Enter language: '))
    list_of_lang.append(temp_set)

for lang in list_of_lang:
    all_know |= lang

for lang in list_of_lang:
    one_know ^= lang

print(len(all_know))
print(list(all_know))
print(len(one_know))
print(list(one_know))
