"""
2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
"""

import string


def main():

    print('Введите произвольное предложение')
    msg = input()
    words = ''
    max_word = ''
    max_len = 0

    for i in msg:
        if i not in string.punctuation:
            words = words + i
    words = words.split()

    for i in words:
        if len(i) > max_len:
            max_len = len(i)
            max_word = i

    print("Самое длинное слово:", max_word, ", его длина составляет", max_len, "символов")


main()
