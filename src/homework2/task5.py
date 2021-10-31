'''
5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
'''


def main():

    print('Введите n-ое число Фибоначчи')
    n = int(input())
    x = 1
    y = 1
    result = 0
    i = 3

    if n < 3:
        result = 1
    else:
        while i <= n:
            result = x + y
            x = y
            y = result
            i = i + 1

    print('n-ое число Фибоначчи =', result)


main()
