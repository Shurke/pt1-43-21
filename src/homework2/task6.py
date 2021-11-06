''' 6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).

Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
'''

entered_number = int(input('Try to enter a polindrome! '))
reversed_number = 0
counter = entered_number

while counter > 0:
    last_number = counter % 10
    reversed_number = 10 * reversed_number + last_number
    counter //= 10

if entered_number == reversed_number:
    print('It is polindrome!')
else:
    print('It is not polindrome(')
