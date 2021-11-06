"""
 Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
 Учитывать только английские буквы.
"""
import string


def main():
    str1 = input("Введите Вашу строку ")
    lower_count = 0
    upper_count = 0
    for i in str1:
        if i in string.ascii_uppercase:
            upper_count += 1
        if i in string.ascii_lowercase:
            lower_count += 1
    print('lower', lower_count, '\n', 'upper', upper_count)


main()
