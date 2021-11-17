"""Каждый из N школьников некоторой школы знает Mi языков. Определите,
 какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник."""


union = set()
all = set()

for i in range(int(input('введите колличество школьников:', ))):
    m = int(input('введите колличество языков школьников:', ))
    a = {input('введите название языков школьника:', ) for j in range(m)}
    all.update(a)
    if i != 1:
        union.update(a)
    else:
        union &= a

print('колличество языков которые знают все школьники:', len(union))
print('\n'.join(sorted(union)))
print('колличество языков которое знает хотя бы один школьник:', len(all))
print('\n'.join(sorted(all)))



