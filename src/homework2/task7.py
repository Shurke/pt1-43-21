side1 = float(input("Сторона 1: "))
side2 = float(input("Сторона 2: "))
side3 = float(input("Сторона 3: "))
if side1 > 0 and side2 > 0 and side3 > 0:
    p = (side1 + side2 + side3) / 2
    if side1 >= side2 and side1 >= side3:
        if side1 < side2 + side3:
            print("Существует!")
            S = (p * (p - side1)*(p - side2) * (p - side3)) ** 0.5
            print(f"Площадь: {S}")
        else:
            print("Не существует!")
    elif side2 >= side1 and side2 >= side3:
        if side2 < side1 + side3:
            print("Существует!")
            S = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
            print(f"Площадь: {S}")
        else:
            print("Не существует!")
    else:
        if side3 < side1 + side2:
            print("Существует!")
            S = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
            print(f"Площадь: {S}")
        else:
            print("Не существует!")
else:
    print("Ошибка ввода!")
