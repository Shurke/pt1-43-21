"""
Задача со звездочкой.

Реализовать функцию, на вход которой передается имя логической функции
(т.е. функция, которая принимает логические параметры и возвращает логическое
значение. Пример: И, ИЛИ, исключающее ИЛИ и т.д.) и набор аргументов, и
возвращает строку, представляющую таблицу истинности функции.

Пример ввода: some_func("AND", A, B)

Правила форматирования:
    • Переменные должны называться A, B, C, D ... и так далее, в том же порядке,
    в котором они передаются в логическую функцию.
    • Параметров не будет больше 26 (A ... Z)
    • Логические значения будут представлены либо 1 (истина), либо 0 (ложь).

Первая строка будет состоять из следующих частей:
    • имена переменных, разделенные пробелом ()
    • два символа табуляции
    • имя функции, параметры которой в круглых скобках разделены запятыми
    • два символа новой строки

Следующие строки будут состоять из следующих по порядку:
    • значения переменных, разделенные пробелом
    • два символа табуляции
    • результат функции для этого расположения переменных
    • символ новой строки
"""

import re


def value_table(operator_name, argument_names):
    """Функция для расчета таблиц истинности."""

    def symbol_place_finding(itter, column):
        """Установка позицции элемента в строке аргументов."""
        if itter & (1 << column):
            flag = 1
        else:
            flag = 0
        return flag

    def get_result(value, flag, name):
        """Получение результата в зависимости от заданной лиогической функции."""
        if value == -1:
            value = flag
        else:
            # Получение результата по заданному оператору
            if name == 'AND':
                value = value & flag
            elif name == 'XOR':
                value = value ^ flag
            elif name == 'OR':
                value = value | flag
        return value

    # Печать заголовной строки
    print(' '.join(argument_names) + '\t' * 2 + operator_name, sep='', end='')
    print('(' + ','.join(argument_names) + ')' + '\n' * 2, sep='')

    number_itter = 1 << len(argument_names)

    # Проход таблицы по строкам
    for row in range(0, number_itter):
        out_value = -1

        # Проход строк по символам слева
        for column_number in range(len(argument_names) - 1, -1, -1):
            symbol_flag = symbol_place_finding(row, column_number)
            out_value = get_result(out_value, symbol_flag, operator_name)

            # Печать символа таблицы
            print(symbol_flag, end=' ')

        # Печать результата строки символов
        print('\t' * 2, out_value)
    return


my_string = re.split(', | |,', input('Введите имя логической функции, и имена аргументов: '))
logic_function, variables = my_string[0], my_string[1:]
value_table(logic_function, variables)
