M = int(input("Введите руб: "))
N = int(input("Введите коп: "))
S = int(input("Введите количество: "))

total = (M * 100 + N) * S
print(f'Общая цена {total // 100} рублей {total % 100} коп')
