"""Task4"""
import string


def main():
    """Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

    Учитывать только английские буквы.
    """
    input_str = input("Введите любую строку: ")
    processed_str = input_str.replace(' ', '')
    list_of_letters = list(processed_str)
    sum_l = 0
    sum_u = 0
    for letter in processed_str:
        if letter in string.ascii_letters:
            if letter.islower():
                sum_l += 1
            if letter.isupper():
                sum_u += 1
    print("Общее количество строчных(маленьких)букв равняется", sum_l)
    print("Общее количество прописных(больших)букв равняется", sum_u)


if __name__ == "__main__":
    main()
