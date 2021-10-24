from string import ascii_letters

a = input('Введите строку ')
c = 0
d = 0
for i in a.replace(' ', ''):
    if i in ascii_letters:
        if i.isupper():
            c = c + 1
        else:
            d = d + 1
print('Количество прописных букв (En):', c, '\nКоличество маленьких букв (En):', d)
