"""
Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
"""

num = int(input('Enter num: '))


def near_two_pow(number, pow_=0):
    num_bin = int(bin(number)[2:])
    while num_bin // 10:
        num_bin //= 10
        pow_ += 1

    def min_dev(a, b):
        for i in range(b, -1, -1):
            if a % pow(2, i) == 0:
                break
        return pow(2, i)

    return min_dev(number, pow_)


print(near_two_pow(num))
