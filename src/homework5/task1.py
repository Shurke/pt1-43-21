"""
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
а значениями кубы этих чисел.
"""


def main():
    my_dictionary = {i: i ** 3 for i in range(1, 21)}
    print(my_dictionary)


if __name__ == "__main__":
    main()