"""
 Вводится M рублей и N копеек цена, а также количество S товара
 Посчитайте общую цену в рублях и копейках за L товаров.
"""


def main():
    ruble = int(input("стоимость товара (рубли) "))
    penny = int(input("Введите стоимость товара (копейки) "))
    volume = int(input("Введите количество товара "))
    ruble_result = volume * (ruble * 100 + penny) // 100
    penny_result = volume * (ruble * 100 + penny) % 100
    print(ruble_result, 'руб.', penny_result, 'коп.')


main()
