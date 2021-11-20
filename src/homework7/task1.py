"""
1.	Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
a.	runner() – все фукнции вызываются по очереди
b.	runner(‘func_name’) – вызывается только функцию func_name.
c.	runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import t1_home
import t2_home
import t3_home
import t4_home
import t5_home
import t6_home
import t7_home
import t8_home
import t8_1_home
import t8_2_home
import t8_3_home
import t8_4_home


def runner():
    t1_home.func()
    t2_home.func()
    t3_home.func()
    t4_home.func()
    t5_home.func()
    t6_home.func()
    t7_home.func()
    t8_home.func()
    t8_1_home.func()
    t8_2_home.func()
    t8_3_home.func()
    t8_4_home.func()


runner()
