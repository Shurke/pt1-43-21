# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.
def main():
    s = input("Введите Вашу строку ")
    lower_count = 0
    upper_count = 0
    for i in s:
        if 'A' <= i <= 'Z':
            upper_count += 1
        if 'a' <= i <= 'z':
            lower_count += 1
    print('lower', lower_count, '\n', 'upper', upper_count)


main()
