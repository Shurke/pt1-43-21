a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b)) * (p - c)
    s1 = s ** (0.5)
    print('это не треугольник площадь которого', s1)
else:
    print('это не треугольник')
