"""
Даны два списка чисел. Посчитайте,
сколько различных чисел входит только в один из этих списков
"""


list1 = input("Введите первый список чисел через пробел: ")
list2 = input("Введите второй список чисел через пробел: ")
general_set = set(list1.split()) | set(list2.split())
num = int(input("Для какого списка зотите посчитать числа? (1 или 2): "))
if num == 1:
    diff_set = general_set - set(list2)
    print(len(diff_set))
elif num == 2:
    diff_set = general_set - set(list1)
    print(len(diff_set))
else:
    print("Ошибка ввода!")
