"""Проект Эйлера. Задача 463.
Обобщите указанную задачу на свое усмотрение, решите ее, покройте тестами.
решение https://oeis.org/A239447"""


A = {0: 0, 1: 1, 2: 2, 3: 5}


def a(n):
    a_n = A.get(n)
    if a_n is not None:
        return a_n

    q, r = divmod(n, 4)

    if r == 0:
        a_n = a(q*2)*6 - a(q)*5 - a(q - 1)*3 - 1
    elif r == 1:
        a_n = a(q*2 + 1)*2 + a(q*2)*4 - a(q)*6 - a(q - 1)*2 - 1
    elif r == 2:
        a_n = a(q*2 + 1)*3 + a(q*2)*3 - a(q)*6 - a(q - 1)*2 - 1
    else:
        a_n = a(q*2 + 1)*6 - a(q)*8 - 1

    A[n] = a_n

    return a_n


print(a(8))
print(a(100))
print(a(3**37))
