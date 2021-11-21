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


def run_function(func_name, module=None):
    if module is None:
        f = getattr(tasks_homework2, func_name, None)
        if f is None:
            f = getattr(tasks_homework4, func_name, None)
            if f is None:
                f = getattr(tasks_homework5, func_name, None)
                if f is None:
                    print(f"Функция {func_name} не найдена")
                    return
        print(f)
        f()
    else:
        f = getattr(module, func_name)
        print(f)
        f()


def run_all_functions(module):
    for function_name in dir(module):
        if function_name[0] != "_" and function_name[:2] != "__":
            run_function(function_name, module)


def runner(*args):
    if len(args) == 0:
        run_all_functions(tasks_homework2)
        run_all_functions(tasks_homework4)
        run_all_functions(tasks_homework5)
    else:
        for item in args:
            run_function(item)


runner("task6_4")
runner("task1_2", "task2_2")
runner()
