""" Задача 7. Оглянемся назад. Числа

Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
алгоритма Евклида (мы не знаем функции и рекурсию).

"""
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите вторе число: "))
except ValueError:
    exit(print("Это не число"))

while number1 != 0 and number2 != 0:
    if number1 > number2:
        number1 = number1 % number2
    else:
        number2 = number2 % number1
print(number1) if number1 != 0 else print(number2)
