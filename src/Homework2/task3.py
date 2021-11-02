"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"
"""

my_string = input('Введите строку: ')
my_string_out = ''
for i in my_string:
    if  i not in my_string_out and i != ' ':
        my_string_out += i
print(my_string_out)
