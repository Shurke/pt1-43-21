import func_collection


def runner(*args):

    functions = [func_name for func_name in dir(func_collection) if not func_name.startswith('__')]
    if not len(args):
        for function in functions:
            print(f'Выполняется функция {function}:')
            func = getattr(func_collection, function)
            print(func.__doc__)
            func()
    else:
        for function in args:
            func = getattr(func_collection, function)
            func()


runner()
