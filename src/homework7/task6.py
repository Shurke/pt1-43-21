'''
Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
'''


def main():
    in_val = int(input('Введите число:'))
    max_power = 1
    max_val = 2
    while max_val < in_val:
        max_val *= 2
        max_power += 1
    max_power -= 1
    max_val = max_val // 2
    if max_val - in_val < in_val - max_val * 2:
        print('Ближайшая степень:', max_power + 1, 'Ближайшее число:', max_val * 2)
    else:
        print('Ближайшая степень:', max_power, 'Ближайшее число:', max_val)


main()
