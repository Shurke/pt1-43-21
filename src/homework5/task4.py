"""
4.	Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
"""


list1 = [1, 3, 5, 11]
list2 = [7, 5, 1]
so = set(list1 + list2)
s1 = so - set(list1)
print('Различных чисел во втором множестве: ', len(s1))
s2 = so - set(list2)
print('Различных чисел в первом множестве: ', len(s2))
