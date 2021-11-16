"""
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или
большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


import string

my_string = input("Введите строку:\n")
for symbol in my_string:
    if symbol in string.punctuation:
        my_string = my_string.replace(symbol, "")
my_list = my_string.split()
set_of_words = set(my_list)
print(f"Всего различных слов: {len(set_of_words)}")
