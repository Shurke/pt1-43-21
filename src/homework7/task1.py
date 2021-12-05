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
    inst_hw2 = HW2()
    inst_hw4 = HW4()
    inst_hw5 = HW5()
    if len(args) > 0:
        for func in args:
            if hasattr(HW2, func):
                getattr(HW2, func)(inst_hw2)
            elif hasattr(HW4, func):
                getattr(HW4, func)(inst_hw4)
            elif hasattr(HW5, func):
                getattr(HW5, func)(inst_hw5)
            else:
                print('Функции ', func, 'не существует.')
    else:
        for func in method_list_hw2:
            getattr(HW2, func)(inst_hw2)
        for func in method_list_hw4:
            getattr(HW4, func)(inst_hw4)
        for func in method_list_hw5:
            getattr(HW5, func)(inst_hw5)


runner()
