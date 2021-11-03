"""
Упорядоченный список.

Дан список целых чисел. Требуется переместить все ненулевые
элементы в левую часть списка, не меняя их порядок, а все
нули - в правую часть. Порядок ненулевых элементов изменять
нельзя, дополнительный список использовать нельзя, задачу
нужно выполнить за один проход по списку. Распечатайте
полученный список.
"""

numb_zero = 0
new_list = list(input('Введите список целых чисел через пробел: ').split())
for i in range(len(new_list), 0, -1):
    if new_list[i-1] == '0':
        new_list.pop(i-1)
        numb_zero += 1
new_list.extend('0'*numb_zero)
print('Упорядоченный список: ', " ".join(map(str, new_list)))
