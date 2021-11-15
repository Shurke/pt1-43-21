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
    words_lst = []

    for i in msg:
        if i not in string.punctuation:
            words = words + i
        else:
            words = words + ' '
    words_lst = words.split()
    max_word = max(words_lst, key=len)

    print("Самое длинное слово:", max_word, ", его длина составляет", len(max_word), "символов")


main()
