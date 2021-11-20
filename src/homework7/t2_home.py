"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Улучшенный вариант
"""

import string


def func():
    a = input('Введите строку: ')
    b = ""
    for i in a:
        if i not in string.punctuation:
            b = b + i
        else:
            b = b + " "
    c = b.replace("  ", " ")
    d = c.split(" ")
    print('самое длинное слово: ', max(d, key=len))


if __name__ == "__main__":
    func()
