"""Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел."""

dict1 = {i: i ** 3 for i in range(1, 21)}

print(dict1)
