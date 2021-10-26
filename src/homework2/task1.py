M = float(input("Рублей: "))
N = float(input("Копеек: "))
S = int(input("Количество товара: "))
K = int(input("Расчитать для: "))
if M >= 0 and N >= 0 and S > 0 and K > 0:
    price = (float(M) + (float(N) / 100)) / S * K
    M = int(price)
    N = int((price - M) * 100)
    print(f"Общая цена: {M}руб. {N}коп.")
else:
    print("Ошибка ввода!")
