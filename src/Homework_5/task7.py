"""
Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
"""


# O(N)
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
NOD = 0

while num_1 != 0:
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    elif num_2 % num_1 == 0:
        NOD = num_1
        break
    else:
        num_2 %= num_1

print(NOD)
