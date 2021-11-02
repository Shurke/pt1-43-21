"""
 Даны: три стороны треугольника.
 Требуется: проверить, действительно ли это стороны треугольника.
 Если стороны определяют треугольник, найти его площадь.
 Если нет, вывести сообщение о неверных данных.
"""

import math


def main():
    first = int(input("Введите 1 сторону треугольника "))
    second = int(input("Введите 2 сторону треугольника "))
    third = int(input("Введите 3 сторону треугольника "))
    if first + second > third and first + third > second and second + third > first:
        p = (first + second + third) / 2
        print(math.sqrt(p * (p - first) * (p - second) * (p - third)))
    else:
        print("Error, Wrong input data format, please try again!")


main()
