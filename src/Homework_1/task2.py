"""
2. Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
Задачу поместите в файл task2.py в папке src/homework2.
"""


import string

sentence = (input("Введите строку: ")).split()
word, max_len = '', 0

for i in sentence:
    value = i.strip(string.punctuation)
    if len(value) > max_len:
        max_len = len(value)
        word = value

print(f"Самое длинное слово - '{word}'")
