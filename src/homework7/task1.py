"""Задача 1.
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим
модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


import tasks_homework2
import tasks_homework4
import tasks_homework5


def run_function(func_name, module):
    """Запускает функиию по имени func_name из модуля module"""
    f = getattr(module, func_name)
    print(f)
    f()


def add_dict_of_functions(module):
    """Добавляет элементы в словарь

    ключ - это имя функции, значение - это модуль

    """

    for function_name in dir(module):
        if function_name[0] != "_" and function_name[:2] != "__":
            dict_of_functions[function_name] = module


def runner(*args):
    if len(args) == 0:
        for function_name, module in dict_of_functions.items():
            run_function(function_name, module)
    else:
        for function_name in args:
            module = dict_of_functions.get(function_name)
            if module:
                run_function(function_name, module)


dict_of_functions = {}
add_dict_of_functions(tasks_homework2)
add_dict_of_functions(tasks_homework4)
add_dict_of_functions(tasks_homework5)
runner("task6_4")
runner("task1_2", "task2_2")
runner()
