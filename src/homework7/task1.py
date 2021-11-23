"""Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


from hw2 import HW2
from hw4 import HW4
from hw5 import HW5


def runner(*args):
    method_list_hw2 = ([func for func in dir(HW2)
                        if callable(getattr(HW2, func)) and not func.startswith("__")])
    method_list_hw4 = ([func for func in dir(HW4)
                        if callable(getattr(HW4, func)) and not func.startswith("__")])
    method_list_hw5 = ([func for func in dir(HW5)
                        if callable(getattr(HW5, func)) and not func.startswith("__")])
    function_mappings = {
        'hw2_task1': HW2.hw2_task1,
        'hw2_task2': HW2.hw2_task2,
        'hw2_task3': HW2.hw2_task3,
        'hw4_task1': HW4.hw4_task1,
        'hw4_task2': HW4.hw4_task2,
        'hw4_task3': HW4.hw4_task3,
        'hw5_task1': HW5.hw5_task1,
        'hw5_task2': HW5.hw5_task2,
        'hw5_task3': HW5.hw5_task3
    }
    inst_hw2 = HW2()
    inst_hw4 = HW4()
    inst_hw5 = HW5()
    if len(args) > 0:
        for func in args:
            if hasattr(HW2, func):
                function_mappings[func](inst_hw2)
            elif hasattr(HW4, func):
                function_mappings[func](inst_hw4)
            elif hasattr(HW5, func):
                function_mappings[func](inst_hw5)
            else:
                print('Функции ', func, 'не существует.')
    else:
        for func in method_list_hw2:
            function_mappings[func](inst_hw2)
        for func in method_list_hw4:
            function_mappings[func](inst_hw4)
        for func in method_list_hw5:
            function_mappings[func](inst_hw5)


runner()
