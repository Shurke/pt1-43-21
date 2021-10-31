''' 7. Даны: три стороны треугольника.

Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют #треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
'''

side_a = int(input('Введите сторону а: '))
side_b = int(input('Введите сторону b: '))
side_c = int(input('Введите сторону c: '))

if (side_a < side_b + side_c) and (side_b < side_a + side_c) and (side_c < side_a + side_b):
    half_perimeter = (side_a + side_b + side_c) / 2
    triangle_square = ((half_perimeter *
                        ((half_perimeter - side_a)
                            * (half_perimeter - side_b)
                            * (half_perimeter - side_c))
                        ) ** 0.5)  # Формула Герона для площади треугольника
    print('Площадь треугольника: ' + str(triangle_square))
else:
    print('Треугольника с заданными сторонами не существует.')
