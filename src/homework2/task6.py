# 6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины. Задача требует работать только с числами
# (без конвертации числа в строку или что-нибудь еще)

a = int(input('Try to enter a polindrome! '))
count = 0
list_a = []
list_b = []
while a > 0:
    b = (a % 10)
    list_a.append(b)
    a //= 10
    count += 1

# print(count)
# print(lista)
for i in reversed(list_a):
    list_b.append(i)
# print(listb)
if list_a == list_b:
    print('It is polindrome!')
else:
    print('It is not polindrome(')
