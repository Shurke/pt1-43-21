"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
"""

import string

my_string = input('Введите предложение: ')
my_string_wo_punctuation = ''
for i in my_string:
    if i in string.punctuation:
        my_string_wo_punctuation += ' '
    else:
        my_string_wo_punctuation = my_string_wo_punctuation + i
max_len_word = max(my_string_wo_punctuation.split(), key=len)
print('Самое длинное слово:', max_len_word)
