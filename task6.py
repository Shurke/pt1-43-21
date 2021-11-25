"""Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)"""

int1 = int(input('введите число: ', ))
int1_2 = int1
int1_1 = int1
int_min = 0
int_max = 0

while int1_2 >= 2:
    if int1_2 & (int1_2 - 1):
        int1_2 = int1_2 - 1
    else:
        int_min = int1_2
        break

while int1_1 <= int1_1 * 2:
    if int1_1 & (int1_1 - 1):
        int1_1 = int1_1 + 1
    else:
        int_max = int1_1
        break

if int1 - int_min > int_max - int1:
    print('ближайшее число степени 2: ', int_max)
else:
    print('ближайшее число степени 2: ', int_min)
