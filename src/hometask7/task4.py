"""
Двоичная пирамида.
На вход функции передаются два целых числа m и n,
такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
Перевести числа от m до n (включительно) в двоичные числа.
Сложить полученные двоичные числа по основанию 10.
Перевести результат сложения в двоичную число.
Вернуть строку с результатом.
"""


def binary_pyramid(left_border_num, right_border_num):
    """returns the result of some binary operations

    (sum_of_the_binary_numbers)

    """

    list_of_binary_numbers = []
    for iter_ in range(left_border_num, right_border_num + 1):
        list_of_binary_numbers.append(int(bin(iter_)[2:]))
    sum_of_the_binary_numbers = sum(list_of_binary_numbers)
    return bin(sum_of_the_binary_numbers)[2:]


def main():
    print('Введите два числа:')
    left_border_num = int(input('Первое число - '))
    right_border_num = int(input('Второе число - '))
    print('Результат равен -', binary_pyramid(left_border_num, right_border_num))


main()
