import string

"""4. Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.
Задачу поместите в файл task4.py в папке src/homework2."""

str = input('Enter string: ')
low = 0
cap = 0

for i in str:
    if i.lower() in string.ascii_lowercase:
        low += i.islower()
        cap += i.isupper()
print("Lowercase - ", low, "\n", "Capitalize - ", cap, sep='')
