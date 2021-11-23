"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


import homework2
import homework4
import homework5


all_homeworks_funcs = {
    homework2: [homework2.task1(),
                homework2.task2(),
                homework2.task3(),
                homework2.task4(),
                homework2.task5(),
                homework2.task6(),
                homework2.task7(),
                homework2.task8_1(),
                homework2.task8_2(),
                homework2.task8_3(),
                homework2.task8_4(),
                homework2.task8_5()],
    homework4: [homework4.task1(),
                homework4.task2(),
                homework4.task3(),
                homework4.task4(),
                homework4.task5(),
                homework4.task6()],
    homework5: [homework5.task1(),
                homework5.task2(),
                homework5.task3(),
                homework5.task4(),
                homework5.task5(),
                homework5.task6(),
                homework5.task7()]}


def runner(*args):
    if len(args) == 0:
        for elem in all_homeworks_funcs.values():
            for func in elem:
                print(func)
    else:
        for arg in args:
            print(arg)


runner(homework2.task2(), homework2.task3(), homework4.task4(), homework5.task5())