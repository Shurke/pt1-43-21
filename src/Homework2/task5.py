"""
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""

number_fib = int(input('Введите номер числа Фибоначчи: '))
previous_number = 0
current_number = 1
temp_number = 0
i = 3
while i <= number_fib:
    temp_number = current_number
    current_number = current_number + previous_number
    previous_number = temp_number
    i += 1
if number_fib == 0:
    print('Неверно введен номер числа')
elif number_fib == 1:
    print(number_fib, '-ое число Фибоначчи: 0', sep='')
else:
    print(number_fib, '-ое число Фибоначчи: ', current_number, sep='')
