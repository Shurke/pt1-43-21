'''
1.Dict comprehensions
Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел.
'''


def main():
    dct = {element: element * element * element for element in range(1, 21)}
    print(dct)


main()
