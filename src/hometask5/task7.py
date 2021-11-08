"""
Даны два натуральных числа. Вычислите их
наибольший общий делитель
при помощи алгоритма Евклида
(мы не знаем функции и рекурсию)
"""


def main():
    n = int(input('Введите первое число: '))
    m = int(input('Введите второе число: '))
    if n > m:
        n, m = m, n
    prev1 = n
    prev2 = m
    c = prev1
    while prev1 % prev2 > 0:
        prev1 = prev2
        prev2 = c % prev2
        c = prev1
    print('НОД равен -', prev2)


main()
