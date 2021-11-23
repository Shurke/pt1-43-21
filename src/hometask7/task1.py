# -*- coding: cp1251 -*-
"""
Оформите решение задач из прошлых
домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули,
getattr и setattr)
runner() - все фукнции вызываются по очереди
runner('func_name') –
вызывается только функцию func_name.
runner('func', 'func1'...) -
вызывает все переданные функции
"""


import hometasks2_functions
import hometasks4_functions
import hometasks5_functions


def call_function(functions_to_be_called):
    """calls all the functions, that are listed in modules"""

    for function in functions_to_be_called:
        if function in dir(hometasks2_functions):
            getattr(hometasks2_functions, function)()
        elif function in dir(hometasks4_functions):
            getattr(hometasks4_functions, function)()
        else:
            getattr(hometasks5_functions, function)()


def all_functions_call():
    """calls all functions from modules - 2, 4, 5"""

    for functions in dir(hometasks2_functions):
        if functions[:2] != '__':
            getattr(hometasks2_functions, functions)()

    for functions in dir(hometasks4_functions):
        if functions[:2] != '__':
            getattr(hometasks4_functions, functions)()

    for functions in dir(hometasks5_functions):
        if functions[:2] != '__':
            getattr(hometasks5_functions, functions)()


def runner(*args):
    """runs all functions that are called"""

    if len(args) == 0:
        all_functions_call()
    else:
        call_function(args)


def main():
    print('runner(func1) result - ')
    runner('set_intersection')
    print('runner(func1, func2) result - ')
    runner('set_xor', 'fizz_buzz_print')
    print('runner() result - ')
    runner()


main()
