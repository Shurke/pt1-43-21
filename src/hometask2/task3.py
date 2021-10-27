# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
def main():
    s = input("Введите строку")
    s = s.replace(' ', '')
    c = s[0]
    ans = c
    for i in s[1:]:
        if i == c:
            continue
        else:
            ans += i
        c = i
    print(ans)


main()
