"""
    Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner. (все станет проще когда мы изучим
    модули, getattr и setattr)

        a. runner() – все фукнции вызываются по очереди
        b. runner(‘func_name’) – вызывается только функцию func_name.
        c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import task1_2
import task1_4
import task1_5


def runner():
    """Вызов функций"""

    def get_task(task_name, modul_name):
        """Выделение в импортированном модуле пользовательских функций."""
        attr_list = dir(modul_name)
        for item in attr_list:
            if not item.startswith('__') and 'task' in item:
                task_name[item] = modul_name
        return task_name

    def func_print(func_dict):
        """Вывод списка доступных функций."""
        print('Доступные функции:')
        for key_item in func_dict:
            temp_func = getattr(func_dict.get(key_item), key_item)
            print(key_item, temp_func.__doc__)
        return

    def func_select(func_dict):
        """Итерфейс выбора доступных функций."""
        print('Выберите через запятую название(я) '
              'функции для запуска или нажмите Enter для запуска всех функций: ')
        input_func = [item for item in input().split(',')]
        out_func = ['All']
        if input_func[0] != '':
            out_func = []
            for item in input_func:
                if item not in func_dict.keys():
                    print('Функция', item, 'отсутствует в списке доступных функций!')
                else:
                    out_func.append(item)
        return out_func

    def start_runner(input_list, func_dict):
        """Вызов функций."""
        if len(input_list) > 0 and input_list[0] == 'All':
            # Запуск всех доступных функций
            for key_item in func_dict:
                temp_func = getattr(func_dict.get(key_item), key_item)
                temp_func()
        elif len(input_list) > 0:
            # Запуск выбранного списка функций
            for item in input_list:
                temp_func = getattr(func_dict.get(item), item)
                temp_func()
        return

    task_dict = {}
    for import_modul_name in [task1_2, task1_4, task1_5]:
        get_task(task_dict, import_modul_name)
    func_print(task_dict)
    task_list = func_select(task_dict)
    start_runner(task_list, task_dict)


runner()
