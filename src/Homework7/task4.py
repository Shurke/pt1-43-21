"""
    Двоичная пирамида

    На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
    Функция выполняет следующие действия:
        a. Перевести числа от m до n (включительно) в двоичные числа.
        b. Сложить полученные двоичные числа по основанию 10.
        c. Перевести результат сложения в двоичную число.
        d. Вернуть строку с результатом.

    Пример:

    func(1, 4)   -->  1111010
        1  // 1 в двоичном виде 1
        +  10  // 2 в двоичном виде 10
        +  11  // 3 в двоичном виде 11
        + 100  // 4 в двоичном виде 100
        -----
        122  // 122 в двоичном виде 1111010
"""


def bin_pyramid(number_1, number_2):
    """Обработка числа."""
    sum_bin = int(format(number_1, 'b'))
    for item in range(number_2, number_2 + 1):
        sum_bin += int(format(item, 'b'))
    return format(sum_bin, 'b')


print('Введите границы диапазона чисел через пробел: ', end='')
try:
    first_number_str, end_number_str = input().split()
    first_number = int(first_number_str)
    end_number = int(end_number_str)
    print('Выходное значение двоичной пирамиды: ', bin_pyramid(first_number, end_number))
except ValueError:
    print('Ошибка! Должны быть введены два числа!')
