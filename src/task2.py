"""
Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
"""
str1 = input("Введите любое предложение: ")
str1 = str1.split()
max_word = ""
max_word_len = 0
for v in str1:
    if len(v) > max_word_len:
        # max_word_len = len(v) 
        max_word = v
print('Самое длинное слово в предложении: ', max_word)
