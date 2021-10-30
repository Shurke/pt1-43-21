"""Task3"""


def main():
    """Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.

    Например, если было введено "abc cde def", то должно быть выведено "abcdef".
    """
    str_ = input('Введите предложение: ')
    str_ = str_.replace(' ', '')
    str_ = list(str_)
    new_st = ''
    for letter in str_:
        if new_st.find(letter) == -1:
            new_st += letter
    print(new_st)


if __name__ == "__main__":
    main()
