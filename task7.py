"""Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)."""


def func(int1):
    int1_2 = int1
    int_min = 0

    if int1 % 2 != 0:
        print('введенное число не делиться на 2')
    else:
        while int1_2 >= 2:
            if int1_2 & (int1_2 - 1):
                int1_2 = int1_2 - 1
            elif int1 % int1_2 != 0:
                int1_2 = int1_2 - 1
            else:
                int_min = int1_2
                break

    print('максимальный делитель, являющийся степенью двойки', int_min)


func(10)
func(12)
func(16)
