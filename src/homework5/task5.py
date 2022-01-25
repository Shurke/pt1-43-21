'''Написать программу которая находит ближайшую степень двойки к
введенному числу. 10(8), 20(16), 1(1), 13(16)
'''


def power_of_two(num):
    i = 1
    closest_power = num
    while closest_power != 1:
        closest_power = closest_power >> 1
        i += 1
    if abs(num - (2 ** (i - 1))) <= abs(num - 2 ** i):
        print(2 ** (i - 1))
    else:
        print(2 ** i)
    return


power_of_two(10)
power_of_two(20)
power_of_two(1)
power_of_two(13)
