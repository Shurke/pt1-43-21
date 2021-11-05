"""Задача 1, Dict comprehensions

Создайте словарь с помощью генератора словарей, так чтобы его ключами
были числа от 1 до 20, а значениями кубы этих чисел.
"""


dict1 = {x: x**3 for x in range(1, 21)}
for key, item in dict1.items():
    print(key, ":", item)
