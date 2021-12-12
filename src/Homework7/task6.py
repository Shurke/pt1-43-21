"""
Написать программу, которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def find_degree(numb):

    def sum_bit(arg):
        """Побитное увеличение на 1."""
        item = 1
        while arg & item != 0:
            arg = arg & ~ item
            item = item << 1
        arg = arg | item
        return arg

    def get_result(div_min, div_max, item_1):
        """Определение степени двойки, ближайшей к заданному числу."""
        if div_min == div_max:
            print('Ближайшие степени двойки к этому числу:', item_1, 'и', item_1 << 1)
        elif div_min >= div_max:
            print('Ближайшая степень двойки к этому числу:', item_1 << 1)
        else:
            print('Ближайшая степень двойки к этому числу:', degree_item_1)
        return

    degree_item_1 = 1
    number_item = numb
    degree_item_2 = 1

    while number_item > 1:
        number_item = number_item >> 1
        degree_item_1 = degree_item_1 << 1  # Поиск степени двойки снизу
        degree_item_2 = (degree_item_2 << 1) ^ 1  # Поиск степени двойки сверху минус 1

    remaind_div_min = degree_item_1 ^ numb  # Промежуток до степени снизу
    remaind_div_max = degree_item_2 & (~ numb)  # Промежуток до степени сверху
    remaind_div_max = sum_bit(remaind_div_max)  # Прибавление единицы

    get_result(remaind_div_min, remaind_div_max, degree_item_1)
    return


my_number = int(input('Введите целое число: '))
find_degree(my_number)
