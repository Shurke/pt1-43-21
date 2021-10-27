"""7. Даны: три стороны треугольника. Требуется: проверить, действительно ли это
стороны треугольника. Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
Задачу поместите в файл task7.py в папке src/homework2."""

a, b, c = [int(input('Enter side length: ')) for _ in range(3)]

if (a + b > c) and (b + c > a) and (a + c > b):
    p = (a + b + c) / 2
    print('Area of the triangle is: ', round(((p * (p - a) * (p - b) * (p - c))**0.5), 2))
else:
    print('Triangle doesn\'t exist!')
