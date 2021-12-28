'''
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''

import math


def pair_counter_func(number_input: str = '1 1 1 1') -> int:
    '''counts pairs in num_list'''

    number_input = number_input.replace(' ', '')
    counted_numbers = []
    pair_counter = 0

    for item in number_input:
        if item not in counted_numbers:
            element_counter = number_input.count(item)

            # Находим количетсво пар через сочетания
            pair_counter += math.factorial(element_counter) \
                // (2 * math.factorial(element_counter - 2))

            counted_numbers.append(item)  # Убираем числа, для которых пары посчитаны

    return pair_counter  # Количество пар элементов равных друг другу


pair_counter_func()
