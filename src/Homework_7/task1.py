import HW1_tasks
import HW4_tasks
import HW5_tasks

list_of_module = [HW1_tasks, HW4_tasks, HW5_tasks]
dict_of_funcs = {}

# Create dictionary with key as function name
# and value as module name
for mod in list_of_module:
    # seek and add to list values that contain 'task' in the name
    for func in list(filter(lambda x: 'task' in x, dir(mod))):
        dict_of_funcs[func] = mod


def runner(*args):
    """Function call every function from imported modules, or calling sent as args function"""
    if len(args) == 0:
        for function, module in dict_of_funcs.items():
            print('Module name: ', module.__name__, '\n',
                  'Function name: ', function, '\n',
                  'Function output: ', '\n', getattr(module, function)(), '\n', sep='')
    else:
        """If args contain the name of function, we gets values this functions only"""
        for function in args:
            module = dict_of_funcs.get(function)
            if module:
                print('Module name: ', module.__name__, '\n',
                      'Function name: ', function, '\n',
                      'Function output: ', '\n', getattr(module, function)(), '\n', sep='')
            else:
                print(f'Function named "{function}" does not exist!')


runner()
