"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)
"""


def search(num):
    diff = 0
    index = 0
    power = 1
    while power <= num:
        if num % power == 0:
            diff = power
        power = 2 ** index
        index += 1
    return diff


my_num = int(input("Введите число: "))
print(f"Максимальный делитель, являющийся степенью двойки: {search(my_num)}")
