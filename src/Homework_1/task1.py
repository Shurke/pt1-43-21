M, N, S = int(input("Введите руб: ")), int(input("Введите коп: ")), int(input("Введите количество: "))

total = (M * 100 + N) * S

print(f'Общая цена {total // 100} рублей {total % 100} коп')