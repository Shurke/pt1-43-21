""" Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. """


def main():
    str1 = input("Введите строку ").replace(' ', '')
    ans = ''
    for i in str1:
        if i not in ans:
            ans += i
    print(ans)


main()
