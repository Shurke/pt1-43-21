"""Даны: три стороны треугольника. Требуется: проверить, 
действительно ли это стороны треугольника. Если стороны определяют треугольник, 
найти его площадь. Если нет, вывести сообщение о неверных данных. """


a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b)) * (p - c)
    s1 = s ** (0.5)
    print('это треугольник площадь которого', s1)
else:
    print('это не треугольник')
