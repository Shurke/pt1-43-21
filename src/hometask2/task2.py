#  Найти самое длинное слово в введенном предложении.
import string


def main():
    s = input("Введите строку")
    result_string = ''
    for i in range(len(s)):
        if s[i] not in string.punctuation:
            result_string += s[i]
        else:
            result_string += ' '
    a = result_string.split()
    max_len = 0
    ans = ''
    for i in a:
        if len(i) > max_len:
            max_len = len(i)
            ans = i
    print(ans)


main()
