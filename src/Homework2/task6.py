"""
Определите, является ли число палиндромом (читается слева
направо и справа налево одинаково). Число положительное
целое, произвольной длины. Задача требует работать только
с числами (без конвертации числа в строку или что-нибудь
еще)
"""

my_number = int(input('Введите число: '))
invert_my_number = 0
reminder = my_number
while reminder > 0:
    invert_my_number = invert_my_number * 10 + reminder % 10
    reminder = reminder // 10
if my_number == invert_my_number:
    print('Число', my_number, 'палиндром')
else:
    print('Число', my_number, 'не палиндром')
