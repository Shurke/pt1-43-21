"""Task4"""


def main():
    """Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

    Учитывать только английские буквы.
    """
    st = input("Введите любую строку: ")
    st = st.replace(' ', '')
    st = list(st)
    sum_l = 0
    sum_u = 0
    english_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in st:
        if english_letters.find(letter) != -1:
            if letter == letter.lower():
                sum_l += 1
            if letter == letter.upper():
                sum_u += 1
    print("Общее количество строчных(маленьких)букв равняется", sum_l)
    print("Общее количество прописных(больших)букв равняется", sum_u)


if __name__ == "__main__":
    main()
