"""Task2
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
 """

import string


def main():
    str1 = input("Введите любое предложение: ")
    for punct in string.punctuation:
        str1 = str1.replace(punct, '')
    str1 = str1.split()
    max_word = ""
    max_word_len = 0
    for word in str1:
        if len(word) > max_word_len:
            max_word_len = len(word)
            max_word = word
    print('Самое длинное слово в предложении:', max_word, '. Его длина', max_word_len, 'символов.')


if __name__ == "__main__":
    main()
