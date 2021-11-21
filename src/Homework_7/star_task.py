"""
Реализовать функцию, на вход которой передается имя логической функции (т.е. функция, которая
принимает логические параметры и возвращает логическое значение.
Пример: И, ИЛИ, исключающее ИЛИ и т.д.) и набор аргументов, и возвращает строку, представляющую
таблицу истинности функции.
Пример ввода: some_func("AND", A, B)
Правила форматирования:
Переменные должны называться A, B, C, D ... и так далее, в том же порядке, в котором они передаются
в логическую функцию.
Параметров не будет больше 26 (A ... Z)
Логические значения будут представлены либо 1 (истина), либо 0 (ложь).
Первая строка будет состоять из следующих частей:
имена переменных, разделенные пробелом ()
два символа табуляции
имя функции, параметры которой в круглых скобках разделены запятыми
два символа новой строки
Следующие строки будут состоять из следующих по порядку:
значения переменных, разделенные пробелом
два символа табуляции
результат функции для этого расположения переменных
символ новой строки
"""


def log_func(func_name, *args):
    length_args = len(args)
    kwargs = {elem: list() for elem in args}
    counter = 0
    while len(bin(counter)[2:]) <= length_args:
        str_ = (length_args - len(bin(counter)[2:])) * '0' + bin(counter)[2:]

        for en, key in enumerate(kwargs):
            kwargs[key].append(int(str_[en]))
        counter += 1

    if func_name == 'AND':
        return and_func(func_name, **kwargs)
    elif func_name == 'OR':
        return or_func(func_name, **kwargs)
    elif func_name == 'XOR':
        return xor_func(func_name, **kwargs)


def and_func(func_name, **kwargs):
    print(*[i for i in kwargs], end='')
    print(' ' * 8, func_name, end='')
    print('(', ','.join([i for i in kwargs]), ')', sep='')
    for i in range(len(kwargs['A'])):
        total = None
        for key in kwargs:
            if total is None:
                total = kwargs[key][i]
            else:
                total &= kwargs[key][i]
            print(kwargs[key][i], end=' ')
        print(' ' * 7, total)


def or_func(func_name, **kwargs):
    print(*[i for i in kwargs], end='')
    print(' ' * 8, func_name, end='')
    print('(', ','.join([i for i in kwargs]), ')', sep='')
    for i in range(len(kwargs['A'])):
        total = None
        for key in kwargs:
            if total is None:
                total = kwargs[key][i]
            else:
                total |= kwargs[key][i]
            print(kwargs[key][i], end=' ')
        print(' ' * 7, total)


def xor_func(func_name, **kwargs):
    print(*[i for i in kwargs], end='')
    print(' ' * 8, func_name, end='')
    print('(', ','.join([i for i in kwargs]), ')', sep='')
    for i in range(len(kwargs['A'])):
        total = 0
        for key in kwargs:
            total += int(kwargs[key][i])
            print(kwargs[key][i], end=' ')
        total = total % 2
        print(' ' * 7, total)


log_func("AND", 'A', 'B', 'C', 'D')
