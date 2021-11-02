"""
 codewars problem ---- Transportation on vacation
 Every day you rent the car costs $40. If you rent the car for 7 or more days,
 you get $50 off your total. Alternatively,
 if you rent the car for 3 or more days, you get $20 off your total.
"""


def main():
    days = int(input("Введите продолжительность отпуска в днях "))
    discount = 0
    if 3 <= days < 7:
        discount = 20
    if days >= 7:
        discount = 50
    print('Итоговая цена', days * 40 - discount)


main()
