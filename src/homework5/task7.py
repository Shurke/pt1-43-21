"""
Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
"""


def main():

    dig1 = int(input('Введите первое натуральное число: '))
    dig2 = int(input('Введите второе натуральное число: '))
    nod = 1
    if dig1 > dig2:
        big = dig1
        small = dig2
    else:
        big = dig2
        small = dig1
    if big % small == 0:
        nod = small
    else:
        while big % small != 0:
            nod = big % small
            big = small
            small = nod
    print('Наибольший общий делитель:', nod)


if __name__ == "__main__":
    main()
