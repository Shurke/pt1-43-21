"""  Найти самое длинное слово в введенном предложении. """
import string


def main():
    str1 = input("Введите строку ").split()
    ans = ''
    max_counter = 0
    for i in str1:
        temp = i.strip(string.punctuation)
        if len(temp) > max_counter:
            max_counter = len(temp)
            ans = temp
    print('Самое длинное слово -', ans)


main()
