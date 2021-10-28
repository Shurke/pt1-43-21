"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.
"""
def main()
    y = input("Введите любую строку: ")
    y = y.replace(' ', '')
    y = list(y)
    sum_l = 0
    sum_u = 0
    english_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for n in y:
        if english_letters.find(n) != -1:
            if n == n.lower():
                sum_l = sum_l + 1
            if n == n.upper():
                sum_u = sum_u + 1
    print("Общее количество строчных(маленьких)букв равняется", sum_l)
    print("Общее количество прописных(больших)букв равняется", sum_u)
    
    if __name__ == "__main__":
    main()
