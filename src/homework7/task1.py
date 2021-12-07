'''
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''

import hw_2
import hw_4
import hw_5


def upd_func_dict(module):
    """Add functions in a dict.

    key - function name
    value - module
    :param module: module name
    :return: Dict of functions

    """

    for f_name in dir(module):
        if 'task_' in f_name:
            common_tasks_dict[f_name] = module


def run_func(f_name):
    if f_name == '' or f_name not in common_tasks_dict.keys():
        print('Func not found')
        return

    module = common_tasks_dict.get(f_name)
    func = getattr(module, f_name, None)

    if func is None:
        print('Func not found')
        return
    else:
        print('Func to execute:', f_name)
        func()


def runner(*args):
    if len(args) == 0:
        for f_name in common_tasks_dict.keys():
            run_func(f_name)
    else:
        for f_name in args:
            run_func(f_name)


common_tasks_dict = {}
upd_func_dict(hw_2)
upd_func_dict(hw_4)
upd_func_dict(hw_5)

runner()
runner('task_2_1', 'task_2_2')
