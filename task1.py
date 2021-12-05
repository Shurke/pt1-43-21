"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import h_w2_4_5


def runner(*args):
    functions = [func_name for func_name in dir(h_w2_4_5) if not func_name.startswith("__")]
    if not len(args):
        for function in functions:
            func = getattr(h_w2_4_5, function)
            func()
    else:
        for function in args:
            func = getattr(h_w2_4_5, function)
            func()


runner('task1_2')
runner('task1_2', 'task3_4')
runner()
