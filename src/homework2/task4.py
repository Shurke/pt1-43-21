'''
4. Посчитать количество строчных (маленьких)
и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
'''

import string


def main():

    print('Введите произвольную строку')
    msg = input()
    eng_lower = 0
    eng_upper = 0

    for i in msg:
        if i in string.ascii_lowercase:
            eng_lower = eng_lower + 1
        elif i in string.ascii_uppercase:
            eng_upper = eng_upper + 1
        else:
            pass

    print('Всего строчных английских букв:', eng_lower)
    print('Всего прописных английских букв:', eng_upper)


main()
