def main():
    '''
    7. Даны: три стороны треугольника.
    Требуется: проверить, действительно ли это стороны треугольника.
    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных.
    '''
    import math

    print('Введите первую длину одной из сторон треугольника:')
    a = float(input())
    print('Введите вторую длину одной из сторон треугольника:')
    b = float(input())
    print('Введите третью длину одной из сторон треугольника:')
    c = float(input())
    if a + b > c and a + c > b and c + b > a:
        print('Такой треугольник существует')
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Его площадь составляет:', s)
    else:
        print('Такого треугольника не существует')

main()