
'''Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''
counter = 1


def dec_counter(fun):

    def wrapper(*args, **kwargs):
        global counter
        res = fun(*args, **kwargs)
        print(f"function called {counter} times yet")
        counter += 1
        return res

    return wrapper


@dec_counter  # декорирование функции
def func(a, b):
    print(a + b)


func(1, 5)
func(1, 5)
func(1, 5)
