"""
Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


nums = int(input('Enter num: '))


def near_two_pow(number, pow_=0):
    num_bin = int(bin(number)[2:])
    while num_bin // 10:
        num_bin //= 10
        pow_ += 1

    def min_pow(a, b):
        if abs(number - pow(2, a)) > abs(number - pow(2, b)):
            return pow(2, b)
        else:
            return pow(2, a)

    return min_pow(pow_, pow_ + 1)


print(near_two_pow(nums))
