"""Задача 8.

Реализовать функцию, на вход которой передается имя логической
функции (т.е. функция, которая принимает логические параметры
и возвращает логическое значение. Пример: И, ИЛИ, исключающее ИЛИ и т.д.)
и набор аргументов, и возвращает строку, представляющую
таблицу истинности функции.
Пример ввода: some_func("AND", A, B)
Правила форматирования:
Переменные должны называться A, B, C, D ... и так далее, в том же порядке,
в котором они передаются в логическую функцию.
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


def get_combinations_of_parameters(number_of_parameters):
    """Возвращает список всех комбинаций таблицы истинности

     для заданнаого колочества параметров

     """
    list_of_combinations = [[0], [1]]
    for i in range(1, number_of_parameters):
        list_of_combinations = list([*x, y] for x in list_of_combinations for y in [0, 1])
    return list_of_combinations


def logic_func(function_name):
    """Возвращает логическую функцию"""
    def logic_and(*args):
        """И"""
        if args.count(0) > 0:
            return 0
        else:
            return 1

    def logic_or(*args):
        """ИЛИ"""
        if args.count(0) == len(args):
            return 0
        else:
            return 1

    def logic_xor(*args):
        """Исключающее ИЛИ"""
        if args.count(1) % 2 == 0:
            return 0
        else:
            return 1

    def logic_imply(*args):
        """Импликация"""
        for i in range(len(args) - 1):
            if args[i] == 1 and args[i+1] == 0:
                return 0
        return 1

    def logic_n_and(*args):
        """Штрих Шеффера, И - НЕ """
        if args.count(1) == len(args):
            return 0
        else:
            return 1

    def logic_n_or(*args):
        """Стрелка Пирса, ИЛИ - НЕ"""
        if args.count(0) == len(args):
            return 1
        else:
            return 0

    def logic_x_n_or(*args):
        """Эквиваленция, Исключающее ИЛИ - НЕ"""
        if args.count(0) == len(args) or args.count(1) == len(args):
            return 1
        else:
            return 0

    if function_name == "AND":
        return logic_and
    elif function_name == "OR":
        return logic_or
    elif function_name == "XOR":
        return logic_xor
    elif function_name == "IMPLY":
        return logic_imply
    elif function_name == "NAND":
        return logic_n_and
    elif function_name == "NOR":
        return logic_n_or
    elif function_name == "XNOR":
        return logic_x_n_or
    else:
        return None


def get_truth_table(function_name, *args):

    number_of_parameters = len(args)
    if number_of_parameters < 2:
        print("Не достачно параметров: нужно хотя бы 2")
        return

    lf = logic_func(function_name)
    if not lf:
        print("Указанная логическая функция не задана.")
        return

    list_of_combinations = get_combinations_of_parameters(number_of_parameters)
    string_of_result = " ".join(args) + "\t" + "\t" + function_name
    string_of_result = string_of_result + "(" + ",".join(args) + ")" + "\n" + "\n"

    for item in list_of_combinations:
        logical_result = lf(*item)
        string_of_result = string_of_result + " ".join(map(str, item)) + "\t"
        string_of_result = string_of_result + "\t" + str(logical_result) + "\n"
    print(string_of_result)


get_truth_table("AND", "A", "B")
get_truth_table("OR", "A", "B", "C", "D")
get_truth_table("XOR", "A", "B")
get_truth_table("XOR", "A", "B", "C")
get_truth_table("IMPLY", "A", "B", "C")
get_truth_table("IMPLY", "A", "B")
get_truth_table("NAND", "A", "B")
get_truth_table("NAND", "A", "B", "C")
get_truth_table("AND", "A", "B", "C")
get_truth_table("NOR", "A", "B")
get_truth_table("XNOR", "A", "B")
