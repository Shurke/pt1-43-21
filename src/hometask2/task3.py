""" Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. """


def main():
    str1 = input("Введите строку ")
    str1 = str1.replace(' ', '')
    prev = str1[0]
    ans = prev
    for i in str1[1:]:
        if i != prev:
            ans += i
        prev = i
    print(ans)


main()
