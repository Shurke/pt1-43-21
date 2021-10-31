''' 2. Найти самое длинное слово в введенном предложении.

Учтите что в предложении есть знаки препинания.
'''

import string

entered_text = input('Enter text, please - ')

stripped = entered_text.translate(str.maketrans('', '', string.punctuation))
entered_text = stripped.split(' ')

max_lenght = 0
longest_word = ''
for word in entered_text:
    if len(word) > max_lenght:
        max_lenght = len(word)
        longest_word = word

print(longest_word)
