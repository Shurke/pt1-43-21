"""
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество S товара Посчитайте общую цену в рублях и копейках за L
товаров.
"""
def main():
    price = float(input("Введите цену товара: "))
    qty = int(input("Введите количество товара:  "))
    print("Сумма равняется: ", price * qty)
    
if __name__ == "__main__":
     main()
