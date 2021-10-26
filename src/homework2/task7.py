# Даны: три стороны треугольника. Требуется: проверить,
# действительно ли это стороны треугольника. Если стороны
# определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.

def main():
    a = input("введите строну a: ")
    try:
        a = float(a)
    except ValueError:
        print("Это не число!")
        return

    b = input("введите строну b: ")
    try:
        b = float(b)
    except ValueError:
        print("Это не число!")
        return
    c = input("введите строну c: ")
    try:
        c = float(c)
    except ValueError:
        print("Это не число!")
        return
    if a < 0 or b < 0 or c < 0:
        print("Стороны не должны быть отрицательными")
        return
    if a+b <= c or a+c <= b or c+b <= a:
        print("Это не треугольник")
    else:
        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))**(1/2)
        print("площадь", s)


main()
