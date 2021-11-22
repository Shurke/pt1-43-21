"""Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)
"""


def main():
    number = int(input('Введите число '))
    power_of_two = 0
    while True:
        if number % 2 == 0:
            number /= 2
            power_of_two += 1
        elif number % 2 != 0:
            if power_of_two == 0:
                print("Делитель отсутствует")
            break
    max_divisor = 2 ** power_of_two
    if power_of_two != 0:
        print(f"Максимальный делитель: {max_divisor}")


if __name__ == "__main__":
    main()
