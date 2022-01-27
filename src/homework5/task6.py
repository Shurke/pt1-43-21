'''Вводится число найти его максимальный делитель, являющийся
степенью двойки. 10(2) 16(16), 12(4).
'''


def max_div(n):
    i = 0
    div = 1
    while not n % div:
        div = div << 1
        i += 1
    div = 2 ** (i - 1)
    return div


print(max_div(10))
print(max_div(16))
print(max_div(12))
