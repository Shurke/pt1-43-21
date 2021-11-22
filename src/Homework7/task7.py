"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)
"""

my_number = int(input('Введите целое число: '))
degree_item = 1
number_item = my_number
while number_item & 1 == 0:  # Ищем, пока в двоичной записи числа не найдется '1'
    degree_item = degree_item << 1
    number_item = number_item >> 1
print('Максимальный делитель числа, который является степенью двойки: ', degree_item)
