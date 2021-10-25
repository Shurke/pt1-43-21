def main():
    m = input("Введите Рубли: ")
    try:
        m = int(m)
    except ValueError:
        print("Это не число!")
        return
    n = input("Введите копейки: ")
    try:
        n = int(n)
    except ValueError:
        print("Это не число!")
        return
    k = input("Введите количество товара: ")
    try:
        k = int(k)
    except ValueError:
        print("Это не число!")
        return
    sum_rub = m * k + n * k // 100
    sum_k = n * k % 100
    print("стоимость товара: ", sum_rub, "р.", sum_k, "к.")


main()
