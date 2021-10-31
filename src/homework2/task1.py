''' 1. Напишите программу, которая считает общую цену.

Вводится M рублей и N копеек цена, а также количество S товара Посчитайте
общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
'''

cost_rubles = input('Enter the cost, rubles - ')

while not cost_rubles.isnumeric():
    print('Please enter a positive number.')
    cost_rubles = input('Enter the cost, rubles - ')
else:
    print('Thanks!')

cost_copecks = input('Enter the cost, copecks - ')

while not cost_copecks.isnumeric() or int(cost_copecks) > 99:
    print('Please enter a positive number from 0 to 99')
    cost_copecks = input('Enter the cost, copecks - ')
else:
    print('Thanks!')

print('Cost of one item is - ' + cost_rubles + ' rubles ' + cost_copecks + ' copecks')

quantity = input('Enter the quantity - ')
while not quantity.isnumeric():
    print('Please enter a positive number.')
    quantity = input('Enter the quantity - ')
else:
    print('Thanks!')

print('Wait for it...')

cost_rubles = int(cost_rubles)
cost_copecks = int(cost_copecks)
quantity = int(quantity)

value_copecks = (cost_rubles * 100 + cost_copecks) * quantity
rubles_part = value_copecks // 100  # Total value, rubles
copecks_part = value_copecks % 100  # Total value, copecks
print('Total value: ' + str(rubles_part) + ' rubles ' + str(copecks_part) + ' copecks.')
