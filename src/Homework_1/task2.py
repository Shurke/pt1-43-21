import string

"""2. Найти самое длинное слово в введенном предложении. Учтите что в предложении
есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
Задачу поместите в файл task2.py в папке src/homework2."""

str = input("Введите строку: ")
word, max_len = '', 0

for i in str.split():
    if len(i.strip(string.punctuation)) > max_len:
        max_len = len(i.strip(string.punctuation))
        word = i.strip(string.punctuation)

print(f"Самое длинное слово - '{word}'")
