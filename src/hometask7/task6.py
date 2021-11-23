"""
Написать программу которая находит ближайшую
степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def nearest_binary_power(num):
    """
    searches nearest_binary_power to number
    """

    num_pow = 0
    num_for_while = num
    while num_for_while > 0:
        num_for_while >>= 1
        num_pow += 1
    return num_pow if abs(2 ** num_pow - num) < abs(2 ** (num_pow - 1) - num) else num_pow - 1


def main():
    input_number = int(input('Введите число '))
    print('Ближайшая степень двойки к введенному числу -', end=' ')
    print(2 ** nearest_binary_power(input_number))


main()
