
'''Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''


def dec_counter(sum_func):

    def wrapper(*args, **kwargs):
        res = sum_func(*args, **kwargs)
        with open('dec_counter_call_history.txt', 'a') as fh:  # Открываем файл на дозапись
            fh.write(f'Function result - {res}.\n')
        fh.close()
        return res
    return wrapper


@dec_counter
def sum_func(a, b):
    '''Суммирует числа a и b'''
    return a + b


sum_func(1, 5)
sum_func(3, 5)
sum_func(1, 4)
