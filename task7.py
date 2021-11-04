a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b)) * (p - c)
s1 = s ** (0.5)
t = str('это треугольник площадь которого')

if a + b > c and b + c > a and a + c > b:
    print(t , s1)
else:
    print('это не треугольник')
