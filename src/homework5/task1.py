'''
1. Dict comprehensions
Создайте словарь с помощью генератора словарей, так
чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
'''


dict_w_cubes = {key: key ** 3 for key in range(1, 21)}
print(dict_w_cubes)
