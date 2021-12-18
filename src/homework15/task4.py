'''Проект Эйлера №451
Обратные по модулю числа

Рассмотрим число 15.
Существует восемь натуральных чисел меньше 15,
которые являются взаимно простыми с 15: 1, 2, 4, 7, 8, 11, 13, 14.
Числами, обратными этим восьми по модулю 15, являются: 1, 8, 4, 13, 2, 11, 7, 14
так как
1*1 mod 15=1
2*8=16 mod 15=1
4*4=16 mod 15=1
7*13=91 mod 15=1
11*11=121 mod 15=1
14*14=196 mod 15=1
Пусть I(n) будет наибольшим положительным числом m меньше n-1, таким что число,
обратное числу m по модулю n равно самому же m.
Таким образом, I(15)=11.
Также, I(100)=51 и I(7)=1.
Найдите ∑I(n) для 3≤n≤2·107
'''


def list_del(a, b):
    '''Находит НОД 2х чисел'''
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def easy_list(n: int = 15) -> list:
    '''Создает список взаимно простых чисел от 1 до n'''
    lst_1 = [el for el in range(1, n) if list_del(n, el) == 1]
    return lst_1


def back_list(list_func: list, n: int) -> list:
    '''Создает список чисел обратных числам из list_func по модулю n в диапазоне от 1 до n-1'''
    list_iter = easy_list(n)
    back_lst = [i for i in list_iter if (i * i) % n == 1 and i < n - 1]
    return back_lst


def max_m(n):
    '''находит наибольшее положительное число m, такое, что число обратное m по модулю n равно самому m'''
    a = easy_list(n)
    b = back_list(a, n)
    m = b[-1]
    return m
    pass


def sum_func(ranges):
    '''Находит Найдите ∑max_m(n) для диапазона ranges'''
    summa = 0
    for i in ranges:
        summa += max_m(i)
    print(summa)
    return summa
    pass


def test1():
    if max_m(15) == 11:
        print('test1 max_m - ok')
    else:
        print('test1 max_m - fail')


def test2():
    if max_m(100) == 51:
        print('test2 max_m - ok')
    else:
        print('test2 max_m - fail')


def test3():
    if max_m(7) == 1:
        print('test3 max_m - ok')
    else:
        print('test3 max_m - fail')


def test4():
    if sum_func(7, 15, 100) == 63:
        print('test4 sum algorithm - ok')
    else:
        print('test4 sum algorithm - fail')


test1()
test2()
test3()
test4()
sum_func(range(3, 2 * 10**7))
