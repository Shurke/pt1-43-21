# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

from string import ascii_letters


def func():
    a = input('Введите строку ')
    c = 0
    d = 0
    for i in a.replace(' ', ''):
        if i in ascii_letters:
            if i.isupper():
                c = c + 1
            else:
                d = d + 1
    print('Количество прописных букв (En):', c, '\nКоличество маленьких букв (En):', d)


if __name__ == "__main__":
    func()
