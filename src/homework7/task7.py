"""
7.	Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def stepen(n):
    global n_max
    n_next = 0
    k = 0
    while n > n_next:
        n_next = 2 ** k
        k += 1
        if n % n_next == 0:
            n_max = n_next
    print(n_max)


stepen(12)
