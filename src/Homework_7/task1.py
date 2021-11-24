import HW1_tasks
import HW4_tasks
import HW5_tasks


def runner(*args):
    list_of_module = [HW1_tasks, HW4_tasks, HW5_tasks]
    if len(args) == 0:
        for module in list_of_module:
            print('*' * 9, '\n', module.__name__, '\n', '*' * 9, '\n', sep='')
            for func in dir(module):
                if 'task' in func:
                    print(func, ':', '\n', getattr(module, func)(), '\n', sep='')
    else:
        for func in args:
            for mod in list_of_module:
                if mod.__name__.lower().startswith(func[:-1]):
                    print(func, ':', '\n', getattr(mod, func)(), '\n', sep='')


runner()
