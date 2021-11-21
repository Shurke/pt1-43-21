'''
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
'''


def main():
    in_val = int(input('Введите число:'))
    max_val = 2
    max_power = 1
    if in_val < 2:
        print("Число должно быть больше либо равно 2")
        return

    while in_val % max_val == 0:
        max_val *= 2
        max_power += 1
    max_val //= 2
    max_power -= 1
    print('Максимальная степень:', max_power, 'Максимальный делитель:', max_val)


main()
