'''Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
'''


def max_2_power_div(num):
    power_of_2 = 0
    float_num = num
    while float_num % 2 == 0:
        float_num /= 2
        power_of_2 += 1
    return print(f'Максимальный делитель числа {num}, являющийся степенью двойки\
 - это {2**power_of_2}')


max_2_power_div(10)
max_2_power_div(16)
max_2_power_div(12)
