"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
Задачу поместите в файл task3.py в папке src/homework2.
"""


str = input('Enter string: ')
result = ''
for i in str.replace(' ', ''):
    if i not in result:
        result += i
print(result)
