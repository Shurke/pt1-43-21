# Даны: три стороны треугольника. Требуется: проверить, действительно ли это
# стороны треугольника. Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.
side1 = float(input("Сторона 1: "))
side2 = float(input("Сторона 2: "))
side3 = float(input("Сторона 3: "))
if side1 > 0 and side2 > 0 and side3 > 0:
    p = (side1 + side2 + side3) / 2
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print("Существует!")
        S = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
        print(f"Площадь: {S}")
    else:
        print("Не существует!")
else:
    print("Ошибка ввода!")
