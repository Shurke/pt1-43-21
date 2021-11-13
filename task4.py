"""Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. 
Учитывать только английские буквы."""


import string

a = str(input('Введите предложение', ))
am = 0
ab = 0

for i in a:
    if i in string.ascii_lowercase:
        am = am + 1
    elif i in string.ascii_uppercase:
        ab = ab + 1

print('больших', ab)
print('маленьких', am)
