"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.
"""

my_string = input('Введите строку: ')
lower_letter = 0
upper_letter = 0
for i in my_string:
    if i.islower():
        lower_letter += 1
    elif i.isupper():
        upper_letter += 1
print('Строчных букв:', lower_letter)
print('Прописных букв:', upper_letter)
