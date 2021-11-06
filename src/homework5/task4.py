'''
Даны два списка чисел. Посчитайте,
сколько различных чисел входит только в один из этих списков
'''


list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 3]

set_difference = set(list_1) | set(list_2)
set_1_diff = set_difference - set(list_2)

print(len(set_1_diff))
