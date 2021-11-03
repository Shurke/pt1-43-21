"""
7.	Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
Задачу поместите в файл task7.py в папке src/homework5.
"""

n = int(input())
m = int(input())
list1 = [m, n]
list1.sort(reverse=True)
i = 0
while list1[i] % list1[i + 1] != 0:
    list1.append(list1[i] % list1[i + 1])
    print(list1)
    list1.sort(reverse=True)
    i += 1
print(list1[i + 1])
