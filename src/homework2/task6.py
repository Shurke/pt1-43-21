''' 6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).

Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
'''

entered_number = int(input('Try to enter a polindrome! '))

list_a = []
list_b = []

while entered_number > 0:
    last_figure = (entered_number % 10)
    list_a.append(last_figure)
    entered_number //= 10

for i in reversed(list_a):
    list_b.append(i)

if list_a == list_b:
    print('It is polindrome!')
else:
    print('It is not polindrome(')
