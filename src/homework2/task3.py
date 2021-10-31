''' 3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.

Например, если было введено "abc cde def", то должно быть выведено "abcdef".
'''

entered_string = input('Enter "abrakadabra"')
str_no_space = entered_string.replace(' ', '')

unique_string = str_no_space[0]
for letter in str_no_space:
    if letter not in unique_string:
        unique_string += letter

print(unique_string)
