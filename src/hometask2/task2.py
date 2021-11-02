"""  Найти самое длинное слово в введенном предложении. """
import string


def main():
    str1 = input("Введите строку ")
    result_string = ''
    for i in str1:
        if i not in string.punctuation:
            result_string += i
        else:
            result_string += ' '
    str2 = result_string.split()
    max_len = 0
    ans = ''
    for i in str2:
        if len(i) > max_len:
            max_len = len(i)
            ans = i
    print(ans)


main()
