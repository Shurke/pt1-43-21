'''
Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
'''


first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))

while first_num % second_num > 0:
    great_comm_divisor = first_num % second_num
    first_num, second_num = second_num, great_comm_divisor

print(f'Greater common divisor of entered numbers is {great_comm_divisor}')
