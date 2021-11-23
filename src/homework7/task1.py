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

hw_2_list = [item for item in dir(hw_2) if 'task_' in item]
hw_4_list = [item for item in dir(hw_4) if 'task_' in item]
hw_5_list = [item for item in dir(hw_5) if 'task_' in item]
common_tasks_list = hw_2_list + hw_4_list + hw_5_list


def run_func(f_name):
    if f_name == '' or f_name not in common_tasks_list:
        print('Func not found')
        return

    func = None
    if f_name.startswith('task_2'):
        func = getattr(hw_2, f_name, None)
    elif f_name.startswith('task_4'):
        func = getattr(hw_4, f_name, None)
    elif f_name.startswith('task_5'):
        func = getattr(hw_5, f_name, None)

    if func is None:
        print('Func not found')
        return
    else:
        print('Func to execute:', f_name)
        func()


def runner(*args):
    if len(args) == 0:
        for item in common_tasks_list:
            run_func(item)
    else:
        for item in args:
            run_func(item)


runner()
runner('task_2_1', 'task_2_2')
