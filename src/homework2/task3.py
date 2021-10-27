# 3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например, если было введено "abc cde def", то #должно быть выведено "abcdef".

st1 = input('Enter "abrakadabra"')
st = st1.replace(' ', '')

a = st[0]
for i in st:
    if i not in a:
        a = a + i

print(a)
