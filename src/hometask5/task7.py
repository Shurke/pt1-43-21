"""
Даны два натуральных числа. Вычислите их
наибольший общий делитель
при помощи алгоритма Евклида
(мы не знаем функции и рекурсию)
"""


def main():
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    if number1 > number2:
        number1, number2 = number2, number1
    prev_number1 = number1
    prev_number2 = number2
    help_number = prev_number1
    while prev_number1 % prev_number2 > 0:
        prev_number1 = prev_number2
        prev_number2 = help_number % prev_number2
        help_number = prev_number1
    print('НОД равен -', prev_number2)


main()
