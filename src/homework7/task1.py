import func_collection


def runner(*args):

    functions = [func_name for func_name in dir(func_collection) if not func_name.startswith('__')]
    if len(args) == 0:
        for function in functions:
            print(f'Выполняется функция {function}:')
            print(function.__doc__)  # Подскажите пожалуйста, как добыть __doc__ из другого модуля?
            func = getattr(func_collection, function)
            func()
    else:
        for function in args:
            func = getattr(func_collection, function)
            func()


runner()
