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
    Sum_Rub = m * k + n * k // 100
    Sum_K = n * k % 100
    print("стоимость товара: ", Sum_Rub, "р.", Sum_K, "к.")

main()
