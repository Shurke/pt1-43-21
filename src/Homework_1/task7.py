a, b, c = [int(input('Enter side length: ')) for _ in range(3)]

if (a + b > c) and (b + c > a) and (a + c > b):
    p = (a + b + c) / 2
    print('Area of the triangle is: ', round(((p * (p - a) * (p - b) * (p - c))**0.5), 2))
else:
    print('Triangle doesn\'t exist!')