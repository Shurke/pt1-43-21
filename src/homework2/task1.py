# 1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также количество S товара Посчитайте #общую цену в рублях и копейках за L товаров.
# Пример:
# Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
# Output: Общая цена 9 рублей 60 копеек

m = input('Enter the cost, rubles - ')

while not m.isnumeric():
    print('Please enter a positive number.')
    m = input('Enter the cost, rubles - ')
else:
    print('Thanks!')

n = input('Enter the cost, copecks - ')

while not n.isnumeric() or int(n) > 99:
    print('Please enter a positive number from 0 to 99')
    n = input('Enter the cost, copecks - ')
else:
    print('Thanks!')

print('Cost of one item is - ' + m + ' rubles ' + n + ' copecks')

s = input('Enter the quantity - ')
while not s.isnumeric():
    print('Please enter a positive number.')
    s = input('Enter the quantity - ')
else:
    print('Thanks!')

print('Wait for it...')

m = int(m)
n = int(n)
s = int(s)

L = (m * 100 + n) * s
L1 = L // 100  # Total value, rubles
L2 = L % 100  # Total value, copecks
print('Total value: ' + str(L1) + ' rubles ' + str(L2) + ' copecks.')
