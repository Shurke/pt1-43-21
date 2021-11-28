'''Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
'''


def closer_2_power(num):
    '''Находит ближайшую степень двойки к числу'''

    power = -1
    bit_num = num

    while bit_num > 0:
        bit_num >>= 1
        power += 1

    if num / (2 ** power) < 1.5:  # Проверяем в меньшую или большую сторону ближе
        return print(f'Ближайшая степень двойки к {num} - это {2**power}')
    else:
        return print(f'Ближайшая степень двойки к {num} - это {2**(power + 1)}')


closer_2_power(10)
closer_2_power(20)
closer_2_power(1)
closer_2_power(13)
