"""Task5"""


def main():
    """Выведите n-ое число Фибоначчи,

    используя только временные переменные,циклические операторы и условные операторы. n - вводится
    """
    num = int(input("Введите N: "))
    if num == 0:
        print('0')
    elif num == 1:
        print('1')
    else:
        prev1 = 0
        prev2 = 1
        index = 3
        while index <= num:
            cur = prev1 + prev2
            index = index + 1
            prev1 = prev2
            prev2 = cur
    print(cur)


if __name__ == "__main__":
    main()
