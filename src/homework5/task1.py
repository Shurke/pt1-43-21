'''
Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел.
'''


def main():
    dct = {int(element1 + 1): (element1 + 1) ** 3 for element1 in range(20)}
    print(dct)


if __name__ == "__main__":
    main()
