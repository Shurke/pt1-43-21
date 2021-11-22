"""
1.	Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
a.	runner() – все фукнции вызываются по очереди
b.	runner(‘func_name’) – вызывается только функцию func_name.
c.	runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import t1_home
import t2_home
import t3_1_home
import t3_2_home
import t3_3_home
import t3_4_home
import t3_5_home
import t3_6_home
import t3_home
import t4_home
import t5_1_home
import t5_2_home
import t5_3_home
import t5_4_home
import t5_5_home
import t5_6_home
import t5_7_home
import t5_home
import t6_home
import t7_home
import t8_1_home
import t8_2_home
import t8_3_home
import t8_4_home
import t8_home

f = [t1_home.func, getattr(t2_home, 'func'), getattr(t3_home, 'func'), getattr(t4_home, 'func'),
     getattr(t5_home, 'func'), getattr(t6_home, 'func'), getattr(t7_home, 'func'),
     getattr(t8_home, 'func'), getattr(t8_1_home, 'func'), getattr(t8_2_home, 'func'),
     getattr(t8_3_home, 'func'), getattr(t8_4_home, 'func'), getattr(t3_1_home, 'func'),
     getattr(t3_2_home, 'func'), getattr(t3_3_home, 'func'), getattr(t3_4_home, 'func'),
     getattr(t3_5_home, 'func'), getattr(t3_6_home, 'func'), getattr(t5_1_home, 'func'),
     getattr(t5_2_home, 'func'), getattr(t5_3_home, 'func'), getattr(t5_4_home, 'func'),
     getattr(t5_5_home, 'func'), getattr(t5_6_home, 'func'), getattr(t5_7_home, 'func')]


def runner(*args):
    if len(args) == 0:
        for function in f:
            function()
    else:
        for name in args:
            for function_ in f:
                if function_.__name__ == name:
                    function_()


runner('func')
