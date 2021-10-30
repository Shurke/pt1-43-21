"""4. Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.
Задачу поместите в файл task4.py в папке src/homework2."""

import string

text = input('Enter string: ')
low_letter = 0
cap_letter = 0

for i in text:
    if i in string.ascii_uppercase:
        cap_letter += 1
    elif i in string.ascii_lowercase:
        low_letter += 1

print("Lowercase letter: ", low_letter, "\n", "Capitalize letter: ", cap_letter, sep='')
