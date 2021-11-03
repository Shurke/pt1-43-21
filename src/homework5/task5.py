"""
5.	Языки
Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
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


n = int(input('Введите количество школьников: '))
s1 = set()
s2 = set()
for item1 in range(n):
    m = int(input('Введите количество языков школьника ' + str(item1 + 1) + ' :'))
    s = {input() for j in range(m)}
    print(s)
    s1.update(s)
    if item1 == 0:
        s2 = s
    else:
        s2 = s2 & s
print(len(s2), '\n', s2)
print(len(s1), '\n', s1)
