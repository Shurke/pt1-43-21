"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


import HW1_tasks
import HW4_tasks
import HW5_tasks
import inspect

HW_funcs = {
    HW1_tasks: [HW1_tasks.task1(),
                HW1_tasks.task2(),
                HW1_tasks.task3(),
                HW1_tasks.task4(),
                HW1_tasks.task5(),
                HW1_tasks.task6(),
                HW1_tasks.task7(),
                HW1_tasks.task8_1(),
                HW1_tasks.task8_2(),
                HW1_tasks.task8_3(),
                HW1_tasks.task8_4(),
                HW1_tasks.task8_5()],
    HW4_tasks: [HW4_tasks.task1(),
                HW4_tasks.task2(),
                HW4_tasks.task3(),
                HW4_tasks.task4(),
                HW4_tasks.task5(),
                HW4_tasks.task6()],
    HW5_tasks: [HW5_tasks.task1(),
                HW5_tasks.task2(),
                HW5_tasks.task3(),
                HW5_tasks.task4(),
                HW5_tasks.task5(),
                HW5_tasks.task6(),
                HW5_tasks.task7()]
    }


def runner(*args):
    if len(args) == 0:
        for elem in HW_funcs.values():
            for func in elem:
                print(func)
    else:
        for arg in args:
            print(arg)


runner(HW1_tasks.task2(), HW1_tasks.task3(), HW4_tasks.task4(), HW5_tasks.task5())
