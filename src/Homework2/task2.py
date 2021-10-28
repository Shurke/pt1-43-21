"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
"""
import string
my_string = input('Введите предложение: ')
my_string_wo = ''
for i in my_string:
    if i in string.punctuation:
        continue
    my_string_wo = my_string_wo + i
word = ''
k = 0
for i in my_string_wo.split():
    if len(i) > k:
        k = len(i)
        word = i
print('Самое длинное слово:', word)
