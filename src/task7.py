"""Task7"""


def main():
    """Даны: три стороны треугольника.

    Требуется: проверить, действительно ли это стороны треугольника.
    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных.
    """
    side1 = float(input("Введите первую сторону треугольника (см): "))
    side2 = float(input("Введите вторую сторону треугольника (см): "))
    side3 = float(input("Введите третью сторону треугольника (см): "))
    if side1 < (side2 + side3) and side2  < (side1 + side3) and side3 < (side1 + side2 ):
        semi_perimeter = (side1 + side2 + side3) / 2   # полупериметр
        # площадь треугольника по формуле Герона
        square = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5
        print("Площадь треугольника равняется (см2)", square)
    else:
        print("Неверные данные")


if __name__ == "__main__":
    main()
