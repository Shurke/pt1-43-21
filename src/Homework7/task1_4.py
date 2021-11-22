"""
    Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner. (все станет проще когда мы изучим
    модули, getattr и setattr)

        a. runner() – все фукнции вызываются по очереди
        b. runner(‘func_name’) – вызывается только функцию func_name.
        c. runner(‘func’, ‘func1’...) - вызывает все переданные функции

    Homework4
"""


def task4_1():
    """FizzBuzz."""
    for item in range(1, 101):
        if item % 3 == 0 and item % 5 == 0:
            print('FizzBuzz')
        elif item % 3 == 0:
            print('Fizz')
        elif item % 5 == 0:
            print('Buzz')
        else:
            print(item)
    return


def task4_2():
    """Работа со списками."""
    list_gener = [i + j for i in ['a', 'b'] for j in ['b', 'c', 'd']]
    print(list_gener)
    print(list_gener[::2])
    list_gener = [str(i + 1) + 'a' for i in range(4)]
    print(list_gener)
    list_gener.remove('2a')
    print(list_gener)
    list_gener_new = list_gener.copy()
    list_gener_new.append('2a')
    print(list_gener_new, list_gener)
    return


def task4_3():
    """Кортеж из одного элемента."""
    new_tuple = ((1, 2, 3), )
    print(len(new_tuple))
    for i in new_tuple:
        for j in i:
            print(j)
    return


def task4_4():
    """Подсчет пар элементов."""
    new_list = list(input('Введите строку из чисел, разделенную пробелами: ').split())
    couple_number = 0
    for i in range(len(new_list)):
        if i - 1 < len(new_list):
            for j in range(i + 1, len(new_list)):
                if new_list[i] == new_list[j]:
                    couple_number += 1
    print('Количество пар: ', couple_number)
    return


def task4_5():
    """Уникальные элементы в списке."""
    new_list = list(input('Введите строку элементов: '))
    out_list = []
    [out_list.append(i) for i in new_list if i not in out_list]
    print('Неповторяющиеся элементы списка: ', " ".join(map(str, out_list)))
    return


def task4_6():
    """Упорядоченный список."""
    numb_zero = 0
    new_list = list(input('Введите список целых чисел через пробел: ').split())
    for i in range(len(new_list), 0, -1):
        if new_list[i - 1] == '0':
            new_list.pop(i - 1)
            numb_zero += 1
    new_list.extend('0' * numb_zero)
    print('Упорядоченный список: ', " ".join(map(str, new_list)))
    return


def func_select(func_list_attr):
    """Интерфейс выбора доступных функций."""
    print('Доступные функции:')
    for item in range(len(func_list_attr)):
        print(func_list_attr[item], globals()[func_list_attr[item]].__doc__)
    print('Выберите через запятую '
          'название(я) функции для запуска или нажмите Enter для запуска всех функций')
    input_str = [item for item in input().split(',')]
    return input_str


def runner(*args):
    """Вызов функций."""
    if len(args) == 0:
        # Запуск всех доступных функций
        [globals()[item]() for item in func_list]
    else:
        # Запуск выбранного списка функций
        [globals()[args[0][item]]() for item in range(len(args[0]))]


# Получение списка пользовательских функций в модуле
attr_list = dir()
# Выбор доступных функций
func_list = [item for item in attr_list if not item.startswith('__') and 'task' in item]
input_func_list = func_select(func_list)

if len(input_func_list) == 1 and input_func_list[0] == '':
    # Запуск всех доступных функций, если при выборе нажат Enter
    runner()
else:
    flag = False
    for item in input_func_list:
        if item not in func_list:
            print('Некорректный ввод')
            flag = True
            break
    if not flag:
        # Запуск списка доступных функций
        runner(input_func_list)
