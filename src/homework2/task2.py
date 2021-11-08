# Найти самое длинное слово в введенном предложении. Учтите что в предложении
# есть знаки препинания.

import string

my_string = input("Введите строку для поиска самого длинного слова:\n")
for x in my_string:
    if x in string.punctuation:
        my_string = my_string.replace(x, "")
result = max(my_string.split(), key=lambda word: len(word))
print(f"Самое длинное слово в предложении: {result}")
