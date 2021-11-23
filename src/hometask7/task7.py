"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_divisor_of_power_of_two(input_number):
    """searches max_divisor_of_power_of_two to number"""

    power_of_two = 1
    answer_number = 1
    while 2 ** power_of_two <= input_number:
        if input_number % 2 ** power_of_two == 0:
            answer_number = 2 ** power_of_two
        power_of_two += 1
    return answer_number


def main():
    input_number = int(input('Введите число '))
    print('Максимальный делитель, являющийся степенью двойки -', end=' ')
    print(max_divisor_of_power_of_two(input_number))


main()
